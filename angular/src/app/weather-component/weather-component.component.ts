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
		styleUrls: ['./weather-component.component.css'],
		providers:[ClimateService]
	}
)
export class WeatherComponentComponent implements OnInit 
{
	climate : any = null;

	constructor(private _climate: ClimateService) { }

	ngOnInit() 
	{
		if(this.climate == null)
		{
			this._climate.getCurrentClimate().subscribe
			(
				climate => 
				{
					this.climate = climate;
					console.log(climate)
				}
			);	
		}	
	}

}
