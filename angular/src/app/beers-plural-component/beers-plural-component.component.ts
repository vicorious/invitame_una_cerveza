import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BeersService } from '../services/beers.service';
import { Beer } from '../dto/beer'

@Component({
  selector: 'app-beers-plural-component',
  templateUrl: './beers-plural-component.component.html',
  styleUrls: ['./beers-plural-component.component.css']
})
export class BeersPluralComponentComponent implements OnInit 
{

  beers : Array<Beer>;
  constructor(private _activate_route: ActivatedRoute, private _beers_service: BeersService) { }

  ngOnInit() 
  {
	  const bar = this._activate_route.snapshot.queryParamMap.get('bar');
	  this.beers = this._beers_service.getBeersDummy(bar);
	  
  }

}
