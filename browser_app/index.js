import 'jquery';
import 'bootstrap';
import 'jquery-form'
import {ConfirmDialog, Dialog} from './confirm-modal.js';

jQuery = window.$ = window.jQuery = require('jquery');
var forge = require('node-forge');
var QRCode = require("qrcode-svg");
var pki = require('node-forge/lib/pki');
var asn1 = require('node-forge/lib/asn1');
var pkcs12 = require('node-forge/lib/pkcs12');
var util = require('node-forge/lib/util');
import SimpleFormSubmit from "simple-form-submit";

const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);


/*
Convert  an ArrayBuffer into a string
from https://developers.google.com/web/updates/2012/06/How-to-convert-ArrayBuffer-to-and-from-String
*/
function ab2str(buf) {
	return String.fromCharCode.apply(null, new Uint8Array(buf));
}


function randBase32() {
	// src: https://en.wikipedia.org/wiki/Base32 RFC4648
	const alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','2', '3', '4', '5', '6', '7'];
	var result = '';
	var buf = new Uint8Array(1);
	for ( var i = 0; i < 16; i++ ) {
		window.crypto.getRandomValues(buf);
		var rand_val = buf[0] & 31;
		result += alphabet[rand_val];
	}
	return result;
}

window.ConfirmDialog = ConfirmDialog;
window.Dialog = Dialog;

window.$(document).ready(function () {
	$('#sidebarCollapse').onclick = function () {
		$('nav.sidebar').classList.toggle('d-none');
	};
});

window.admin = {
	registration: {
		delete: function(href, username) {
			var dialog = new ConfirmDialog('Reject user registration', `Are you sure to reject the registration request from "${username}"?`);
			dialog.show().then(()=>{
				fetch(href, {
					method: 'DELETE'
				});
			});
			return false;
		},
		accept: function(href, username) {
			var dialog = new ConfirmDialog('Accept user registration', `Are you sure to accept the registration request from "${username}"?`);
			dialog.show().then(()=>{
				fetch(href, {
					method: 'PUT'
				});
			});
			return false;

		}

	}
};

window.auth = {
	sign_up: {
		submit: function(form) {
			SimpleFormSubmit.submitForm(form.action, form)
				.then(response =>{
					response.json().then(function(data) {
						if (data.errors) {
							var msg ='<ul>';
							for( var field in data.errors) {
								msg += `<li>${field}: ${data.errors[field]}</li>`;
							}
							msg += '</ul>';
							new Dialog('Registration Error', `Error Happend: ${msg}`).show()
						} else {
							new Dialog('Registration successfully', 'Wait until an administrator has aproved your account').show();
						}
					});
				});
			return false;
		}
	}
};

window.totp = {
	init_list: function(){
	},
	init_new: function() {
		//create new TOTP secret, create qrcode and ask for token.
		var form = $('form');
		var secret = randBase32();
		var input_secret = form.querySelector('#secret')
		if(input_secret.value == '') {
			input_secret.value = secret;
		}

		form.querySelector('#name').onchange=window.totp.generate_qrcode;
		form.querySelector('#name').onkeyup=window.totp.generate_qrcode;
		window.totp.generate_qrcode();
	},
	generate_qrcode: function(){
		var form = $('form');
		var secret = form.querySelector('#secret').value;
		var name = form.querySelector('#name').value;
		var issuer = 'Lenticular%20Cloud';
		var svg_container = $('#svg-container')
		var svg = new QRCode(`otpauth://totp/${issuer}:${name}?secret=${secret}&issuer=${issuer}`).svg();
		var svg_xml =new DOMParser().parseFromString(svg,'text/xml')
		if(svg_container.childNodes.length > 0) {
			svg_container.childNodes[0].replaceWith(svg_xml.childNodes[0])
		} else {
			svg_container.appendChild(svg_xml.childNodes[0]);
		}
		//	.innerHtml=svg;
	}
}

window.fido2 = {
	init: function() {

	}
}
window.password_change= {
	init: function(){
		var form = $('form');
		form.onsubmit = function () {
			SimpleFormSubmit.submitForm(form.action, form)
				.then(response =>{
					response.json().then(function(data) {
						if (data.errors) {
							var msg ='<ul>';
							for( var field in data.errors) {
								msg += `<li>${field}: ${data.errors[field]}</li>`;
							}
							msg += '</ul>';
							new Dialog('Password change Error', `Error Happend: ${msg}`).show()
						} else {
							new Dialog('Password changed', 'Password changed successfully!').show();
						}
					});
				});
			return false;
		}

	}
}
window.oauth2_token = {
	revoke: function(href, id){
		var dialog = new ConfirmDialog('Revoke client tokens', `Are you sure to revoke all tokens from client "${id}"?`);
		dialog.show().then(()=>{
			fetch(href, {
				method: 'DELETE'
			});
		});
		return false;
	}
}



window.client_cert = {
	init_list: function() {
		// do fancy cert stats stuff
	},
	init_new: function() {
		// create localy key or import public key

		var form = $('form#gen-key-form');

	},
	generate_private_key: function() {
		var form = $('form#gen-key-form');
		var key_size = form.querySelector('#key-size').value;
		var valid_time = form.querySelector('input[name=valid_time]').value;
		$('button#generate-key').style['display'] = 'none';
		pki.rsa.generateKeyPair({bits: key_size, workers: 2}, function(err, keypair) {
			console.log(keypair);

			//returns the exported key to a hidden form
			var form_sign_key = $('#gen-key-sign form');
			form_sign_key.querySelector('textarea[name=publickey]').value = pki.publicKeyToPem(keypair.publicKey);
			form_sign_key.querySelector('input[name=valid_time]').value = valid_time;

			SimpleFormSubmit.submitForm(form_sign_key.action, form_sign_key)
				.then(response => {
					response.json().then( response => {
						if (data.errors) {
							var msg ='<ul>';
							for( var field in data.errors) {
								msg += `<li>${field}: ${data.errors[field]}</li>`;
							}
							msg += '</ul>';
							new Dialog('Password change Error', `Error Happend: ${msg}`).show()
						} else {
							// get certificate
							var data = response.data;
							var certs = [
								pki.certificateFromPem(data.cert),
								pki.certificateFromPem(data.ca_cert)
							];
							var password = form.querySelector('#cert-password').value;
							var p12Asn1;
							if (password == '') {
								p12Asn1 = pkcs12.toPkcs12Asn1(keypair.privateKey, certs, null, {algorithm: '3des'}); // without password
							} else {
								p12Asn1 = pkcs12.toPkcs12Asn1(keypair.privateKey, certs, password, {algorithm: '3des'}); // without password
							}
							var p12Der = asn1.toDer(p12Asn1).getBytes();
							var p12b64 = util.encode64(p12Der);


							var button = $('#save-button');
							button.href= "data:application/x-pkcs12;base64," + p12b64
							button.style['display'] ='block';
							//new Dialog('Password changed', 'Password changed successfully!').show();
						}
					});
				});
		});
	},
	revoke_certificate: function(href, id){
		var dialog = new ConfirmDialog('Revoke client certificate', `Are you sure to revoke the certificate with the fingerprint ${id}?`);
		dialog.show().then(()=>{
			fetch(href, {
				method: 'DELETE'
			});
		});
		return false;
	}
};

