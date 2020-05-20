import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { Climate } from '../dto/climate';
import { CatchError} from './catch-error';

//#region Function "regresion_lineal" we could be find in "IA.js" 
declare function regresion_lineal(json) : any;
//#endregion

@Injectable
(
	{
		providedIn: 'root'
	}
)
export class ClimateService 
{

	host 		 : string = "http://api.openweathermap.org/data/2.5/weather";
	host_service : string = "http://localhost:5000/climate/weather"
	ciudad 		 : string = "Bogota";
	API_KEY		 : string = "8cde928e3f9fdc6ce35a4f5d0375ac62";
	
	constructor(private http: HttpClient) { }
	
	/**
	*
	*
	*
	*
	**/
	getCurrentClimate():  Observable<any>
	{
		//TODO This feature going to BACKEND
		//let params = new HttpParams().set('city', this.ciudad)
		return this.http.get(this.host_service + "/" + this.ciudad).pipe
		(
			retry(1),
			catchError(CatchError.handleError)		
		)
		
	}
	
	/**
	*
	*
	*
	*
	**/
	saveClimate(climate : Climate): Observable<any>
	{
		return this.http.post(this.host_service, JSON.stringify(climate)).pipe
		(
			retry(1),
			catchError(CatchError.handleError)		
		)
	}
	
	/**
	*
	* In the BackEnd, the user session var, fill this request
	*
	*
	**/
	calculateBestBeerFromClimateAndTaste(): Observable<any>
	{
		return this.http.get(this.host_service).pipe
		(
			retry(1),
			catchError(CatchError.handleError)			
		)
		
	}
	
	/**
	*
	*
	* This method calculate best beer from taste
	*
	*
	**/
	calculateBeerBeerFromTaste()
	{
		return this.http.get(this.host_service).pipe
		(
			retry(1),
			catchError(CatchError.handleError)			
		)
		
	}	
		
}
