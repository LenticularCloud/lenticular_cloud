"use strict";

const $ = document.querySelector.bind(document)
const _ = document.getElementById

export class Dialog {
	template(){
		return `
		<div class="modal-dialog">
			<div class="modal-content">

				<div class="modal-header">
					<h5 class="modal-title"></h5>
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
				</div>

				<div class="modal-body">
				</div>

				<div class="modal-footer">
					<button type="button" class="btn btn-primary close" data-dismiss="modal">Close</button>
				</div>
			</div>
		</div>`;
	}

	constructor(title, message) {
		this._div = (new DOMParser().parseFromString(this.template(), 'text/html')).body.firstChild;
		this._div.querySelector('.modal-body').innerHTML = message;
	}

	show() {
		var self = this;
		this._promise = new Promise((resolve, reject) => {
			self._resolve = resolve;
			self._reject = reject;
		});

		this._div.querySelectorAll('.close').forEach(function (o){
			o.onclick=self.close.bind(self);
		});

		$('.messages-box').appendChild(this._div);
		return this._promise
	}

	close() {
		this._close()
		this._resolve();
	}

	_close() {
		$('.messages-box').removeChild(this._div);
	}

}



export class ConfirmDialog extends Dialog {
	template(){
		return `
		<div class="modal-dialog">
			<div class="modal-content">

				<div class="modal-header">
					<h5 class="modal-title"></h5>
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
				</div>

				<div class="modal-body">
				</div>

				<div class="modal-footer">
					<button type="button" class="btn btn-danger close" data-dismiss="modal">Cancel</button>
					<button type="button" class="btn btn-primary btn-ok process">Process</button>
				</div>
			</div>
		</div>`;
	}

	show(){
		var self = this;
		this._div.querySelector('.process').onclick = () => {
			self._close();
			self._resolve();
		};
		return super.show()
	}

	close() {
		this._close()
		this._reject('canceled by user');
	}
}
