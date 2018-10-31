$(document).ready(function() {
	//variables
	var contrasena = $('[name=contrasena]');
	var contrasena2 = $('[name=contrasena2]');
	var confirmacion = "Las contraseñas si coinciden";
	var longitud = "La contraseña debe estar formada entre 8-15 carácteres";
	var negacion = "No coinciden las contraseñas";
	var vacio = "La contraseña no puede estar vacía";
	//oculto por defecto el elemento span
	var span = $('<br><span></span>').insertAfter(contrasena2);
	span.hide();
	//función que comprueba las dos contraseñas
	function coincidePassword(){
	var valor1 = contrasena.val();
	var valor2 = contrasena2.val();
	//muestro el span
	span.show().removeClass();
	//condiciones dentro de la función
	if(valor1 != valor2){
	span.text(negacion).addClass('negacion');
	}
	if(valor1.length==0 || valor1==""){
	span.text(vacio).addClass('negacion');
	}
	if(valor1.length<8 || valor1.length>15){
	span.text(longitud).addClass('negacion');
	}
	if(valor1.length!=0 && valor1==valor2){
	span.text(confirmacion).removeClass("negacion").addClass('confirmacion');
	}
	}
	//ejecuto la función al soltar la tecla
	contrasena2.keyup(function(){
	coincidePassword();
	});
});
