import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BarService } from '../services/bar.service';
import { Bar } from '../dto/bar'
	


//#region Function "initPrimero" we could be find in "primera.js" 
declare function initPrimero() : any;
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
	public loading = false;
	bares : Array<Bar>;	 
	constructor(private router: Router, private barService: BarService) { }

	ngOnInit() 
	{
		this.loading = true;		
		initPrimero();
		this.barService.getBars().subscribe
		(
			res => 
			{
				console.log('entro');				
				this.bares = res;
				this.loading = false;
				if(Object.entries(res).length === 1)
				{
					this.router.navigate(['**']);	
				}
			}
		);
	
	}
  
	/**
	*
	* Beers
	*
	**/
	goBeers(bar_name: string)
	{
		this.loading = true;
		setTimeout("<p>a</p>", 10000000);
		this.router.navigate(['/beers'], { queryParams: { bar : bar_name} });	
		this.loading = false;		
	}

}
