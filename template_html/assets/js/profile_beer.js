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
	
	var buttonAdd = document.getElementById("btnSumProduct");
	
	buttonAdd.addEventListener('click', function (event) 
	{	
		event.preventDefault();		
		
		var h2total = document.getElementById("H2total");				
		var olProductos = document.getElementById("olProductos");
		var cantidad = document.getElementById("slCantidad");
		var presentacion = document.getElementById("slPresentacion");	
		var defaultP = document.getElementById("pDefault");
		if(defaultP != null || defaultP != undefined)
		{
			defaultP.remove();
		}
		
		console.log(olProductos.childElementCount)

		for(var i = 0; i < parseInt(cantidad.value); i++) 
		{
			var total = 0;
			var il = document.createElement("li");
			var totalNumerico = presentacion.value 
			il.setAttribute("precio", totalNumerico);
			total += parseInt(totalNumerico)
			var buttonErase = document.createElement("button");
			buttonErase.className += "fa fa-trash eraseElement";
			buttonErase.setAttribute("aria-hidden", true);
			buttonErase.addEventListener('click', function () 
			{			
				console.log("Borrado")			
				console.log(olProductos.childElementCount)
				if(olProductos.childElementCount == 1)
				{
					var defaultPN = document.createElement("p");
					defaultPN.setAttribute("id", "pDefault");
					defaultPN.innerHTML = "No records found...";
					defaultPN.className += "letra negrita";
					olProductos.appendChild(defaultPN);
				}
	
				this.parentNode.remove();
				h2total.innerHTML = (parseInt(h2total.innerHTML) - total)
			});
			il.className += "letra negrita liprecio";			

			il.textContent += presentacion.options[presentacion.selectedIndex].text + " $ " + totalNumerico
			il.appendChild(buttonErase);
			olProductos.appendChild(il);		
			//parseInt(presentacion.value).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');	
			console.log("Cosa tener es: ");
			h2total.innerHTML =  (parseInt(h2total.innerHTML) + total)
		}			

	}, false);	
	
});