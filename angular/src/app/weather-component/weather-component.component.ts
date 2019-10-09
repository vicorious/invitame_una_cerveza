import { Component, OnInit } from '@angular/core';
import { ClimateService } from '../services/climate.service';

//#region Function "formatDateTime" we could be find in "primera.js" 
declare function formatDateTime() : any;
//#endregion

@Component
(
	{
		selector: 'app-weather-component',
		templateUrl: './weather-component.component.html',
		styleUrls: ['./weather-component.component.css']
	}
)
export class WeatherComponentComponent implements OnInit 
{

	constructor(private _climate: ClimateService) { }

	ngOnInit() 
	{
		this._climate.getCurrentClimate().subscribe
		(
			climate => 
			{
				console.log(JSON.stringify(climate))
			}
		);		
	}

}
