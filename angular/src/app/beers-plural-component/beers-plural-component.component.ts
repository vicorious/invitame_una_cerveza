import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { BeersService } from '../services/beers.service';
import { Beer } from '../dto/beer'
import { NgxSpinnerService } from "ngx-spinner";
import { ToastrService } from 'ngx-toastr';
import { faUserTie } from '@fortawesome/free-solid-svg-icons';
import { faBeer } from '@fortawesome/free-solid-svg-icons';
import { faHands } from '@fortawesome/free-solid-svg-icons';
import { BeerService } from '../services/beer.service';

@Component({
  selector: 'app-beers-plural-component',
  templateUrl: './beers-plural-component.component.html',
  styleUrls: ['./beers-plural-component.component.css']
})
export class BeersPluralComponentComponent implements OnInit 
{

	beers : Array<Beer>;
	faUserTie = faUserTie;
	faBeer = faBeer;
	faHands = faHands;
	constructor(private _activate_route: ActivatedRoute, 
				private _beers_service: BeersService, 
				private _beer_service: BeerService,
				private router: Router,
				private spinner: NgxSpinnerService, 
				private toast: ToastrService) { }

	ngOnInit() 
	{
		this.spinner.show();
		const bar = this._activate_route.snapshot.queryParamMap.get('bar');		
		this._beers_service.getBeersByBar(bar).subscribe
		(
			res => 
			{
				this.beers = res;
				this.spinner.hide();

			},
			error =>
			{
				this.toast.error('Error obteniendo cervezas para ${bar}', error);
				this.spinner.hide();

			}
		);	 
	}
	
  	/**
	*
	* Beers
	*
	**/
	goBeerDetail(beer: Beer)
	{
		this._beer_service.beerClearMessage();
		this.spinner.show();
		setTimeout(() => {
			this.spinner.hide();
		  }, 2000);
		
		console.log('A enviar: ', beer)
		this._beer_service.beerMessage(beer);
		console.log('enviado: ', beer)
		this.router.navigate(['/detailbeer'], { queryParams: { beer : beer.id} });		
	}

}
