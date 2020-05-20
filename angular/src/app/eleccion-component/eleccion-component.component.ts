import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';

//Function declared in promotions.js
declare function initChoice(): any;

@Component
(
	{
		selector: 'app-eleccion-component',
		templateUrl: './eleccion-component.component.html',
		styleUrls: ['./eleccion-component.component.css']
	}
)
export class EleccionComponentComponent implements OnInit 
{

	public loading = false;

  	constructor(private router: Router, private toastr: ToastrService) { }

  	ngOnInit() {
		initChoice();
  	}
  
  go(item: any): void
  {
	  this.loading = true;
	  var _route   = "";	  
	  switch(item)
	  {
		  case "master":
			_route = "/bars";
			break;
		  case "promotion":
			_route = "/promotion";
			break;
		  case "curious":
		    _route = "/curious";
			break;
		  default:
		    break;
	  }
	  this.router.navigate([_route]);
	  this.loading = false;	  
	  
  }

  showSuccess() {
    this.toastr.success('Good', 'Easy toast', {
		timeOut: 3000
	  });
  }

}
