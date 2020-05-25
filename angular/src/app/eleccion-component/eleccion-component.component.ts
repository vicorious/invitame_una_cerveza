import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgxSpinnerService } from "ngx-spinner";
import { ToastrService } from 'ngx-toastr';
import { faUserTie } from '@fortawesome/free-solid-svg-icons';
import { faBeer } from '@fortawesome/free-solid-svg-icons';


//Function declared in card_events.js
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

	faUserTie = faUserTie;
	faBeer = faBeer;

  	constructor(private router: Router, private spinner: NgxSpinnerService, private toast: ToastrService) { }

  	ngOnInit() { 
		initChoice(); 
		this.spinner.show();
		setTimeout(() => {
			this.spinner.hide();
		  }, 2000);	
  	}
  
  go(item: any): void
  {
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
	  
  }

  toastTest(){
	this.toast.success('Hello world!', 'Toastr fun!');
  }

}
