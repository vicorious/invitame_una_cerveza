document.addEventListener("DOMContentLoaded", function(event) 
{
	var slider = document.getElementById("myRange");
	var output = document.getElementById("demo");
	var output2 = document.getElementById("demo2");
	output.innerHTML = slider.value;
	output2.innerHTML = "52000";
	slider.oninput = function() 
	{
		output.innerHTML = this.value;
		output2.innerHTML = parseInt(output2.innerHTML) - this.value;
	}
});