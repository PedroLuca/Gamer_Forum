function valid(){
	var pass = document.getElementById("pass").value;
	var name = document.getElementById("name").value;
	var n = pass.length;
	if((n >= 8) && (name != "")){
		var nome = document.getElementById("name").value;
		var msg = "Olá " + nome + "! Obrigado pela ajuda!";
		alert(msg);
	}
}
function login(){
	var password = document.getElementById("password").value;
	var usuario = document.getElementById("username").value;
	if((usuario == "") && (password == "")){
		alert("Preencha todos os campos!");
	}
}