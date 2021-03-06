import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { PromotionService } from '../services/promotion.service';
import { BeerService } from '../services/beer.service';
import { Beer } from '../dto/beer';
import { NgxSpinnerService } from 'ngx-spinner';
import { ToastrService } from 'ngx-toastr';
import { faUserTie, faHands } from '@fortawesome/free-solid-svg-icons';
import { Promotion } from '../dto/promotion';

//Function declared in promotions.js
declare function initPromotions(): any;

@Component({
  selector: 'app-promocion-component',
  templateUrl: './promocion-component.component.html',
  styleUrls: ['./promocion-component.component.css']
})
export class PromocionComponentComponent implements OnInit 
{
  promotions : Array<Promotion>;
  faUserTie = faUserTie;
  faHands = faHands;
  
  constructor(private _activate_route: ActivatedRoute, 
              private _promotion_service: PromotionService, 
              private _beer_service: BeerService,
              private router: Router,
              private spinner: NgxSpinnerService, 
              private toast: ToastrService) { }

  ngOnInit() 
  {
    this.spinner.show();
    setTimeout(() => 
    {
        initPromotions();
        this._promotion_service.getPromotions(0).subscribe( promotions =>
        {
            this.promotions = promotions;
        });
			  this.spinner.hide();
		}, 2000);	
  }
  
  setBeer(beer: Beer)
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
