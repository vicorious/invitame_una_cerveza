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

	beers : Array<Beer>;
	constructor(private _activate_route: ActivatedRoute, private _promotion_service: PromotionService, private router: Router) { }

  ngOnInit() 
  {
	 this.beers =  this._promotion_service.getPromotion();
  }
  
  setBeer(beer: Beer)
  {
	  this.router.navigate(['/detailbeer'], { queryParams: { beer : beer.name} });
  }

}
