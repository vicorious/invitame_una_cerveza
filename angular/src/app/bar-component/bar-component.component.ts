import { Component, OnInit } from '@angular/core';


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

  constructor() { }

  ngOnInit() 
  {
	  initPrimero();
  }

}
