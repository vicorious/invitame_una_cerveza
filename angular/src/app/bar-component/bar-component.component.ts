import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BarService } from '../services/bar.service';
import { Bar } from '../dto/bar';
import { NgxSpinnerService } from "ngx-spinner";
import { ToastrService } from 'ngx-toastr';
import { faUserTie } from '@fortawesome/free-solid-svg-icons';
import { faHands } from '@fortawesome/free-solid-svg-icons';


//#region Function "initPrimero" we could be find in "primera.js" 
declare function initBars() : any;
//#endregion

@Component
(
	{
		selector: 'app-bar-component',
		templateUrl: './bar-component.component.html',
		styleUrls: ['./bar-component.component.css']

	}
)

export class BarComponentComponent implements OnInit 
{
	bares : Array<Bar>;
	faUserTie = faUserTie;
	faHands = faHands;
	constructor(private router: Router, private barService: BarService, private spinner: NgxSpinnerService,
				private toast: ToastrService) { }

	ngOnInit() 
	{	
		this.spinner.show();
		initBars();
		this.barService.getBars().subscribe
		(
			res => 
			{				
				this.bares = res;
				this.spinner.hide();

			},
			error =>
			{
				this.toast.error('Error obteniendo bares', error);
				this.spinner.hide();

			}
		);
		
		
	
	}
  
	/**
	*
	* Beers
	*
	**/
	goBeers(_bar_id: string)
	{
		this.router.navigate(['/beers'], { queryParams: { bar : _bar_id} });		
	}

}
