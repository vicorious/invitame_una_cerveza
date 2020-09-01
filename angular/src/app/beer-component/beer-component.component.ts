import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { BeerService } from '../services/beer.service';
import { Beer } from '../dto/beer';
import { NgxSpinnerService } from "ngx-spinner";
import { ToastrService } from 'ngx-toastr';
import { faUserTie } from '@fortawesome/free-solid-svg-icons';
import { faHands } from '@fortawesome/free-solid-svg-icons';
import { faBeer } from '@fortawesome/free-solid-svg-icons';
import { faLongArrowAltRight } from '@fortawesome/free-solid-svg-icons';
import { ParameterService } from '../services/parameter.service';


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
	beer_detail : any;
	beer : any;
	pay_types: any [];

	faUserTie = faUserTie;
	faHands = faHands;
	faBeer = faBeer;
	faSave = faLongArrowAltRight;
	
	constructor(private _activate_route: ActivatedRoute, 
				private router: Router, 
				private _beer_service: BeerService,
				private _parameters_service: ParameterService,
				private spinner: NgxSpinnerService, 
				private toast: ToastrService) { }

	ngOnInit() 
	{
		this.spinner.show();
		setTimeout(() => {
			this._beer_service.beerGetMessage().subscribe(beer => {
				this.beer = beer;
			});

			this._beer_service.getBeerPairing(this.beer.beer.id).subscribe(beer_pairing =>{
				this.beer_detail = beer_pairing;
			});

			this._parameters_service.getPayType().subscribe(payTypes =>{
				this.pay_types = payTypes;
			});

			this.spinner.hide();
		  }, 2000);		
			
	}
	
	goSave() 
	{
		this.spinner.show();
		setTimeout(() => {
			this.spinner.hide();
		  }, 2000);
		this.router.navigate(['/code']);
	}
	

	getBeerDetail(id: number)
	{
		const beer = this._activate_route.snapshot.queryParamMap.get('beer');
		this.beer_name = beer;	
	}		


}
