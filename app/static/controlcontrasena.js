$(document).ready(function()
{



	$('#contrasena').keyup(function()
	{
		$('#result').html(checkStrength($('#contrasena').val()))
	})	
		
	function checkStrength(contrasena)
	{
		var strength = 0
		
		if (contrasena.length < 8) {
			$('#result').removeClass()
			$('#result').addClass('corta')
			return 'Muy corta'
		}
		
		if (contrasena.length > 9) strength += 1
		
		//If password contains both lower and uppercase characters, increase strength value.
		if (contrasena.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/))  strength += 1
		
		//If it has numbers and characters, increase strength value.
		if (contrasena.match(/([a-zA-Z])/) && contrasena.match(/([0-9])/))  strength += 1
		
		//If it has one special character, increase strength value.
		if (contrasena.match(/([!,%,&,@,#,$,^,*,?,_,~])/))  strength += 1
		
		//if it has two special characters, increase strength value.
		if (contrasena.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
		

		
		if (strength < 2 )
		{
			$('#result').removeClass()
			$('#result').addClass('debil')
			return 'Debil'
		}
		else if (strength == 2 )
		{
			$('#result').removeClass()
			$('#result').addClass('buena')
			return 'Buena'
		}
		else
		{
			$('#result').removeClass()
			$('#result').addClass('fuerte')
			return 'Fuerte'
		}
	}
});

