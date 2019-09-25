$(document).ready(function() 
{
	$("#btnNinja").on('click', function()
	{
		alert('Aqui llamamos al cabron que quieras');
	});		
	$("#scan").on('click', function() 
	{
		$("code").html('Scaneado...');
		$('#qr').html5_qrcode(function(data)
		{
			$(".feedback").css('display','block');
		    // do something when code is read
		    $(".feedback").html('<img src="assets/images/yes.png" style="height: 20px"></img> Codigo scaneado como: <strong>' +data +'</strong>');
			var canvas = document.getElementById('canvas');			
			var context = canvas.getContext('2d');
			var video = document.querySelector('video');
			console.log(video);
			context.drawImage(video, 0, 0, 600, 450);			
			$("#qr").html5_qrcode_stop();
			$("#divCanvas").css('display', 'block');
			$("#txtFinal").html('<img src="assets/images/yes.png" style="height: 20px"></img> Codigo scaneado como: <strong>' +data +'</strong>');
			$("code").html('Click "Empezar Scaneo" para <b>Empezar a scanear el codigo QR');
			$(".feedback").css('display','none');
			$("#scan").removeClass('disabled');
			$("#scan").removeAttr('disabled');
			$("#stop").addClass('disabled');
			$("#stop").attr('disabled','disabled');
			$("#change").addClass('disabled');
			$("#change").attr('disabled','disabled');
			$("#codeAccept").css('display', 'block');
			return;
		},
		function(error)
		{
			//show read errors 
			$(".feedback").html('<img src="assets/images/no.png" style="height: 20px"></img> No es posible escanear el codigo! Error: ' +error)
		},
		function(videoError)
		{
			//the video stream could be opened
			$(".feedback").html('<img src="assets/images/no.png" style="height: 20px"></img> Error de video: '+videoError);
		}
		);

		$("#scan").addClass('disabled');
		$("#scan").attr('disabled','disabled');
		$("#stop").removeClass('disabled');
		$("#stop").removeAttr('disabled');
		$("#change").removeClass('disabled');
		$("#change").removeAttr('disabled');
	});

	$("#stop").on('click', function() 
	{
		$("#divCanvas").css('display', 'none');
		$("#codeAccept").css('display', 'none');
		$("#txtFinal").html('');
		$("#qr").html5_qrcode_stop();
		$("code").html('Click "Empezar Scaneo" para <b>Empezar a scanear el codigo QR');

		$("#scan").removeClass('disabled');
		$("#scan").removeAttr('disabled');
		$("#stop").addClass('disabled');
		$("#stop").attr('disabled','disabled');
		$("#change").addClass('disabled');
		$("#change").attr('disabled','disabled');
		$(".feedback").html("");
	});
	$("#change").on('click', function() 
	{
		$("#divCanvas").css('display', 'block');
		$("#codeAccept").css('display', 'none');
		$("#txtFinal").html('');		
		$("#qr").html5_qrcode_changeCamera();

		$("#scan").addClass('disabled');
		$("#scan").attr('disabled','disabled');
		$("#stop").removeClass('disabled');
		$("#stop").removeAttr('disabled');
	});
});