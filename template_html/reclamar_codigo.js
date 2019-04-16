$(document).ready(function() {
	$("#scan").on('click', function() {
		$("code").html('Scaneado...');
		$('#qr').html5_qrcode(function(data){
		         // do something when code is read
		         $(".feedback").html('<img src="yes.png" style="height: 20px"> Codigo scaneado como: <strong>' +data +'</strong>');
		    },
		    function(error){
		        //show read errors 
		        $(".feedback").html('<img src="no.png" style="height: 20px"> No es posible escanear el codigo! Error: ' +error)
		    }, function(videoError){
		        //the video stream could be opened
		        $(".feedback").html('<img src="no.png" style="height: 20px"> Error de video');
		    }
		);

		$("#scan").addClass('disabled');
		$("#stop").removeClass('disabled');
		$("#change").removeClass('disabled');
	});

	$("#stop").on('click', function() {
		$("#qr").html5_qrcode_stop();
		$("code").html('Click "Empezar Scaneo" para <b>Empezar a scanear el codigo QR');

		$("#scan").removeClass('disabled');
		$("#stop").addClass('disabled');
		$("#change").addClass('disabled');
		$(".feedback").html("");
	});
	$("#change").on('click', function() {
		$("#qr").html5_qrcode_changeCamera();

		$("#scan").addClass('disabled');
		$("#stop").removeClass('disabled');
	});
});