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
	
	constructor(private _http: HttpClient) { }
	
	/**
	*
	*
	*
	**/
	getCurrentClimate():  Observable<any>
	{
		let params = new HttpParams().set('q', this.ciudad);
		return this._http.get(this.host, { params: params }).pipe
		(
			retry(1)		
		)
		
	}
	
}
