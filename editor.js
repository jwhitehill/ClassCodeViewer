function callPost () {
	var editor = ace.edit("editor");
	var code = window.btoa(editor.getValue());
	$.ajax({ type: "POST", data: { "type": "send", "code": code } });
}

function startPostThread () {
	setInterval(callPost, 1000);
}
