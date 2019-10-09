import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';

@Injectable
(
	{
		providedIn: 'root'
	}
)
export class ClimateService 
{

	host : string = "http://api.openweathermap.org/data/2.5/weather";
	ciudad : string = "Bogota";
	API_KEY = "8cde928e3f9fdc6ce35a4f5d0375ac62";
	
	constructor(private http: HttpClient) { }
	
	/**
	*
	*
	*
	**/
	getCurrentClimate():  Observable<any>
	{
		let params = new HttpParams().set('q', this.ciudad).set("appid", this.API_KEY).set("units", "metric")
		return this.http.get(this.host, { params: params }).pipe
		(
			retry(1)		
		)
		
	}
	
}
