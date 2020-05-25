"use strict";

const $ = document.querySelector.bind(document)
const _ = document.getElementById

export class ConfirmDialog {

	constructor(message) {
		this._div = document.getElementById('confirm-dialog-template').content.querySelector('div').cloneNode(true);
		this._div.querySelector('.modal-body').innerHTML = message;
	}

	show() {
		var self = this;
		this._promise = new Promise((resolve, reject) => {
			self._resolve = resolve;
			self._reject = reject;
		});

		this._div.querySelectorAll('.close').forEach(function (o){
			o.onclick=self.cancel.bind(self);
		});

		this._div.querySelector('.process').onclick = () => {
			self._close();
			self._resolve();
		};

		$('.messages-box').appendChild(this._div);
		return this._promise
	}

	cancel() {
		this._close()
		this._reject('canceled by user');
	}

	_close() {
		$('.messages-box').removeChild(this._div);
	}

}



