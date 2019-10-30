import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { BeerService } from '../services/beer.service';
import { Beer } from '../dto/beer';

//#region Methos declared in JS file
declare function initProfileBeer(): any;
//#endregion

@Component
(
	{
		selector: 'app-beer-component',
		templateUrl: './beer-component.component.html',
		styleUrls: 
		[
			'./beer-component.component.css'
		]
	}
)
export class BeerComponentComponent implements OnInit 
{
	beer_images: Array<string> = ["assets/images/fondo_perfil_pola.jpg", "assets/images/thepub850.jpg", "assets/images/tommahawk.jpg"]
	beer_image: string;
	beer_name: string;
	beer : Beer;
	public loading = false;
	
	constructor(private _activate_route: ActivatedRoute, private router: Router, private beer_service: BeerService) { }

	ngOnInit() 
	{
		this.loading = true;
		initProfileBeer();		
			
	}
	
	goSave() 
	{		
		this.loading = true;
		this.router.navigate(['/code']);
		this.loading = false;
	}
	
	dummy()
	{
		const beer = this._activate_route.snapshot.queryParamMap.get('beer');
		this.beer_name = beer;
		switch(beer)
		{
			case "Melas doble IIPA":
				this.beer_image = this.beer_images[0];
				break;
			case "IPA The pub":
				this.beer_image = this.beer_images[1];
				break;
			case "Tommahowk IPA":
				this.beer_image = this.beer_images[2];
				break;
			default:
				break;
		}
		this.loading = false;	
	}
	
	getBeerDetail(id: int)
	{
		const beer = this._activate_route.snapshot.queryParamMap.get('beer');
		this.beer_name = beer;
		this.beer = this.beer_service.getBeerForId(id);
	}
  		

}
