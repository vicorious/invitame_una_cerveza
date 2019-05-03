//Constantes
const URL_SERVICIO 	 = "http://api.openweathermap.org/data/2.5/weather?q=";
const APP_URL_KEY	 = "&appid=8cde928e3f9fdc6ce35a4f5d0375ac62";
const KELVIN 		 = 273.15;

/**
*
* Ready DOM!
*
**/
$(document).ready(function()
{
	$("#btnClima").on('click', function()
	{
		consumir_servicio_clima("Bogota");
	});		
	
});

/**
*
* Consumir servicio del clima
*
**/
function consumir_servicio_clima(_ciudad)
{
	$.ajax
	({
        url: URL_SERVICIO + _ciudad + APP_URL_KEY		
    }).then(function(data) 
	{
	   console.log("CLIMA: ");
       console.log(data.weather[0].main);
	   console.log("Tipos de nubes: ");	   
	   console.log(data.weather[0].description);	
	   console.log("Porcentajes de nubes en la ciudad: ");
	   console.log(data.clouds.all + "% of clouds" );	
	   console.log("Timestamp: ");
	   console.log(new Date());
	   console.log("Temperatura CELSIUS: ");
	   console.log(data.main.temp - KELVIN);
	   
    });	
}

