
function Signin() {
	document.getElementById("button1").innerHTML = "Bienvenido, XXXXX";
}

function Signout() {
    document.getElementById("button1").innerHTML = "ADIOS" ;
}

function myFunction(imgs) {
    var expandImg = document.getElementById("expandedImg");
    var imgText = document.getElementById("imgtext");
    expandImg.src = imgs.src;
    imgText.innerHTML = imgs.alt;
    expandImg.parentElement.style.display = "block";
}

function alerta() {
    alert("bienvenido");
}


function validarUsername(username) {
	return(username.trim().length >= 5);
}

function validarNombre(nombre) {
	return(nombre.trim().length >= 2);
}

function validarApellido(apellido) {
	return(apellido.trim().length >= 2);
}

function validarCorreo(correo) {

	return((correo.indexOf("@") > 0) && (correo.lastIndexOf("@") < correo.length-1) && (correo.indexOf("@") == correo.lastIndexOf("@")));
}

function validarTarjeta(tarjeta) {
return( Number.isInteger(Number(tarjeta)) && (tarjeta.trim().length >= 10));
}

function validarContrasena(contrasena) {
	return(contrasena.trim().length >= 5);
}

function validar(formulario) {
	var retorno = true;
	var msj = "";
	if(! validarUsername(formulario["username"].value))
	{
		formulario["username"].focus();
		retorno = false;
		msj += "Escriba al menos 5 caracteres en el campo \"Username\".";
	}
	if(! validarNombre(formulario["nombre"].value))
	{
		formulario["nombre"].focus();
		retorno = false;
		msj += "Escriba al menos 2 caracteres en el campo \"Nombre\".";
	}

	if(! validarApellido(formulario["apellido"].value))
	{
		formulario["apellido"].focus();
		retorno = false;
		msj += "Escriba al menos 2 caracteres en el campo \"Apellido\".";
	}


	if(! validarCorreo(formulario["correo"].value))
	{
		if(retorno)
		{
			formulario["correo"].focus();
			retorno = false;
		}
		else msj += "\n";
		msj += "Escriba una direcci\u00F3n de correo v\u00E1lida en el campo \"Email\".";
	}
	if(! validarTarjeta(formulario["tarjeta"].value))
	{
		if(retorno)
		{
			formulario["tarjeta"].focus();
			retorno = false;
		}
		else msj += "\n";
		msj += "El campo \"tarjeta\" debe tener 10 numeros.";
	}
		if(! validarContrasena(formulario["contrasena"].value))
	{
		formulario["contrasena"].focus();
		retorno = false;
		msj += "el campo \"contrasena\" debe tener minimo 5 caracteres.";
	}


	if(! retorno) alert(msj);

	return(retorno);
}

