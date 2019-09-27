document.addEventListener("DOMContentLoaded", function(event) 
{
	init();
	
});

function init()
{
	sliderFunction();

	paymentType();
	
	priceMarketWork();
					
}


function sliderFunction()
{
	var slider = document.getElementById("myRange");
	var output = document.getElementById("demo");
	var output2 = document.getElementById("demo2");
	let value_input = 100;
	output.innerHTML = slider.value;
	output2.innerHTML = value_input;
	var before_value = slider.value;
	var new_value = 0;
	slider.oninput = function() 
	{			
		if(before_value > this.value)
		{
			output.innerHTML = this.value;
			output2.innerHTML = parseInt(output2.innerHTML) - ( parseInt(before_value) - parseInt(this.value));
			
		}else if (before_value < this.value)
		{
			output.innerHTML = this.value;
			output2.innerHTML = parseInt(output2.innerHTML) + (parseInt(this.value) - parseInt(before_value));			
			
		}		
		new_value = this.value;		
		before_value = new_value;
		
	}
	
}


function paymentType()
{
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
}

function formatMoney(number, decPlaces, decSep, thouSep) 
{
	decPlaces = isNaN(decPlaces = Math.abs(decPlaces)) ? 2 : decPlaces,
	decSep = typeof decSep === "undefined" ? "." : decSep;
	thouSep = typeof thouSep === "undefined" ? "," : thouSep;
	var sign = number < 0 ? "-" : "";
	var i = String(parseInt(number = Math.abs(Number(number) || 0).toFixed(decPlaces)));
	var j = (j = i.length) > 3 ? j % 3 : 0;

	return sign +
		(j ? i.substr(0, j) + thouSep : "") +
		i.substr(j).replace(/(\decSep{3})(?=\decSep)/g, "$1" + thouSep) +
		(decPlaces ? decSep + Math.abs(number - i).toFixed(decPlaces).slice(2) : "");
}

function priceMarketWork()
{
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
				
		for(var i = 0; i < parseInt(cantidad.value); i++) 
		{
			var total = 0;
			var il = document.createElement("li");
			var totalNumerico = parseInt(presentacion.value.replace(",",""))
			il.setAttribute("precio", totalNumerico);
			total += parseInt(totalNumerico)
			var buttonErase = document.createElement("button");
			buttonErase.className += "fa fa-trash eraseElement";
			buttonErase.setAttribute("aria-hidden", true);
			buttonErase.addEventListener('click', function () 
			{			
				if(olProductos.childElementCount == 1)
				{
					var defaultPN = document.createElement("p");
					defaultPN.setAttribute("id", "pDefault");
					defaultPN.innerHTML = "No records found...";
					defaultPN.className += "letra negrita";
					olProductos.appendChild(defaultPN);
				}
				
				h2total.setAttribute("precio", (parseInt(h2total.getAttribute("precio")) - total))
				h2total.innerHTML = "$" + formatMoney(parseInt(h2total.getAttribute("precio")));				
				this.parentNode.remove();

			});
			il.className += "letra negrita liprecio";			

			il.textContent += presentacion.options[presentacion.selectedIndex].text + " $ " + formatMoney(totalNumerico);
			il.appendChild(buttonErase);
			olProductos.appendChild(il);	
			h2total.setAttribute("precio", totalNumerico + parseInt(h2total.getAttribute("precio") == undefined ? "0" : h2total.getAttribute("precio")));
			h2total.innerHTML = "$" + formatMoney(parseInt(h2total.getAttribute("precio")) == undefined ? total : parseInt(h2total.getAttribute("precio")));
		}			

	}, false);	
}
