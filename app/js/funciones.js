
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