/* onclick imagenes index , el color se hace mas opaco*/
function myFunction(imgs) {
    var expandImg = document.getElementById("expandedImg");
    var imgText = document.getElementById("imgtext");
    expandImg.src = imgs.src;
    imgText.innerHTML = imgs.alt;
    expandImg.parentElement.style.display = "block";
}

/* tama;o username >=5 <10*/

function validarUsername(user) {
	return((user.trim().length >= 5) && (user.trim().length <=10) );
}
/* tama;o nombre,apellido >=2 <12*/
function validarNombre(nombre) {
	return((nombre.trim().length >= 2)&&(nombre.trim().length <= 12));
}

function validarApellido(apellido) {
	return((apellido.trim().length >= 2)&&(apellido.trim().length <= 12));
}

function validarCorreo(correo) {

	return((correo.indexOf("@") > 0) && (correo.lastIndexOf("@") < correo.length-1) && (correo.indexOf("@") == correo.lastIndexOf("@")));
}

function validarTarjeta(tarjeta) {
return( Number.isInteger(Number(tarjeta)) && (tarjeta.trim().length = 10));
}

function validarContrasena(contrasena) {
	return(contrasena.trim().length >= 8);

}

function validar(formulario) {
	var retorno = true;
	var msj = "";
	if(! validarUsername(formulario["user"].value))
	{
		formulario["user"].focus();
		retorno = false;
		msj += "Escriba al menos 5 caracteres en el campo \"User\".";
	}
	if(! validarNombre(formulario["nombre"].value))
	{
		formulario["nombre"].focus();
		retorno = false;
		msj += "Escriba entre 2 y 10 caracteres en el campo \"Nombre\".";
	}

	if(! validarApellido(formulario["apellido"].value))
	{
		formulario["apellido"].focus();
		retorno = false;
		msj += "Escriba entre 2 y 10  caracteres en el campo \"Apellido\".";
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
		msj += "el campo \"contrasena\" debe tener minimo 8 caracteres.";
	}


	if(! retorno) alert(msj);

	return(retorno);
}



