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
});