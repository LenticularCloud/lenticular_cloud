import 'jquery';
import 'bootstrap';
import 'jquery-form'

window.$ =window.jQuery = require('jquery');
var forge = require('node-forge');
var QRCode = require("qrcode-svg");
var pki = require('node-forge/lib/pki');
var asn1 = require('node-forge/lib/asn1');
var pkcs12 = require('node-forge/lib/pkcs12');
var util = require('node-forge/lib/util');

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


window.totp = {
	init_list: function(){
	},
	init_new: function() {
		//create new TOTP secret, create qrcode and ask for token.
		var form = $('form');
		var secret = randBase32();
		var input_secret = form.find('#secret')
		if(input_secret.val() == '') {
			input_secret.val(secret);
		}

		form.find('#name').on('change',window.totp.generate_qrcode);
		window.totp.generate_qrcode();
	},
	generate_qrcode: function(){
		var form = $('form');
		var secret = form.find('#secret').val();
		var name = form.find('#name').val();
		var issuer = 'Lenticular%20Cloud';
		var svg_container = $('#svg-container')
		var svg = new QRCode(`otpauth://totp/${issuer}:${name}?secret=${secret}&issuer=${issuer}`).svg();
		svg_container.html(svg);
	}
}

window.fido2 = {
	init: function() {

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
		var key_size = form.find('#key-size').val();
		var valid_time = form.find('input[name=valid_time]').val();
		$('button#generate-key')[0].style['display'] = 'none';
		pki.rsa.generateKeyPair({bits: key_size, workers: 2}, function(err, keypair) {
			console.log(keypair);
			form.data('keypair', keypair);

			//returns the exported key to a hidden form
			var form_sign_key = $('#gen-key-sign form');
			form_sign_key.find('textarea[name=publickey]').val(pki.publicKeyToPem(keypair.publicKey));
			form_sign_key.find('input[name=valid_time]').val(valid_time);

			form_sign_key.ajaxForm({
				success: function(response) {
					// get certificate
					var data = response['data'];

					var certs = [
						pki.certificateFromPem(data.cert),
						pki.certificateFromPem(data.ca_cert)
					];
					var password = form.find('#cert-password').val();
					var keypair = form.data('keypair');
					var p12Asn1;
					if (password == '') {
						p12Asn1 = pkcs12.toPkcs12Asn1(keypair.privateKey, certs, null); // without password
					} else {
						p12Asn1 = pkcs12.toPkcs12Asn1(keypair.privateKey, certs, password, {algorithm: '3des'}); // without password
					}
					var p12Der = asn1.toDer(p12Asn1).getBytes();
					var p12b64 = util.encode64(p12Der);


					var button = $('#save-button')[0];
					button.href= "data:application/x-pkcs12;base64," + p12b64
					button.style['display'] ='block';
				}

			});
			// submit hidden form
			form_sign_key.submit();
		});
	}
};

