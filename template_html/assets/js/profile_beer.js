document.addEventListener("DOMContentLoaded", function(event) 
{
	var slider = document.getElementById("myRange");
	var output = document.getElementById("demo");
	var output2 = document.getElementById("demo2");
	let value_input = 52000;
	output.innerHTML = slider.value;
	output2.innerHTML = value_input;
	let before_value = 0;
	slider.oninput = function() 
	{
		output.innerHTML = this.value;
		output2.innerHTML = parseInt(output2.innerHTML) - this.value;
	}
	
	var select_pago = document.getElementById("selectPago");
	var tarjeta = document.getElementById("divTarjetaCredito");
	var pse = document.getElementById("divPSE");
	select_pago.onchange = function()
	{
		var valor = this.value;
		if(valor === "PSE")
		{
			tarjeta.style.display = 'none';
			pse.style.display = 'block';
		}else
		{
			tarjeta.style.display = 'block';
			pse.style.display = 'none';
		}
	};
	
});