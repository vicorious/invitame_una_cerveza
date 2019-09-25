import { Component, OnInit } from '@angular/core';

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
  constructor() { }

  ngOnInit() 
  {
	  initProfileBeer();
  }
  
  beers = ["Atomic IIPA", "Smash IPA", "Colon IPA", "IPA 'La 15'", "Apostol IPA"]; 
  isavailable = true;

}
