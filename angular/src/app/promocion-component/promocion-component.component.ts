import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { PromotionService } from '../services/promotion.service';
import { Beer } from '../dto/beer'

@Component({
  selector: 'app-promocion-component',
  templateUrl: './promocion-component.component.html',
  styleUrls: ['./promocion-component.component.css']
})
export class PromocionComponentComponent implements OnInit 
{
	public loading = false;
	beers : Array<Beer>;
	constructor(private _activate_route: ActivatedRoute, private _promotion_service: PromotionService, private router: Router) { }

  ngOnInit() 
  {
	 this.loading = true;
	 this.beers =  this._promotion_service.getPromotion();
	 this.loading = false;
  }
  
  setBeer(beer: Beer)
  {
	  this.loading = true;
	  this.router.navigate(['/detailbeer'], { queryParams: { beer : beer.name} });
	  this.loading = false;
  }

}
