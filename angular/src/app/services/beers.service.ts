import { Injectable } from '@angular/core';
import { Beer } from '../dto/beer';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { of } from 'rxjs';
import { CatchError} from './catch-error';

@Injectable

(
	{
		providedIn: 'root'
	}
)
export class BeersService 
{
	public HOST            : string = "http://localhost:5000"
	public URI_BEERS       : string = "/beers";
	public URI_BEER_ID     : string = "/beer/";
	public GET             : string = "/GET";
	public URI_BEER_INSERT : string = "/beer/INSERT";
	public URI_BEER_UPDATE : string = "/beer/UPDATE";
	
	// Http Headers
	httpOptions = 
	{
		headers: new HttpHeaders
		(
			{
				'Content-Type': 'application/json'
			}
		)
	}	
	
	constructor(private http: HttpClient) { }
  
	/**
	*
	*
	*
	*
	**/
	getBeersDummy(bar: string)
	{
		let melas_doble_iipa = new Beer("Melas doble IIPA", "assets/images/beer/melas/atomic_ipa.jpg", "Dulce y amarga cerveza con gran cantidad de alcohol para que en vez de saborearla; ALUCINES la cerveza", "10%");
		let milagrosa_ipa = new Beer("IPA The pub", "assets/images/beer/milagrosa/ipa.jpg", "¡La mejor cerveceria de bogotá con cervezas artesanales del mundo!", "9%");
		let tommahowk_ipa = new Beer("Tommahowk IPA", "assets/images/beer/tierra_santa/cervezas.jpg", "Tenemos todos los estilos de cerveza a todo tiempo y en todo lugar", "8%");	  
		let beer;
		switch(bar)
		{
			case "Melas":
				beer = melas_doble_iipa;
				break;
			case "The pub":
				beer = milagrosa_ipa;
				break;
			case "Tierra santa":
				beer = tommahowk_ipa;
				break;
			default:
				break;
		}
				
		let beers : Beer[] = [beer];
		return beers;
	}
  
	/**
	*
	*
	*
	*
	**/
	getBeers() : Observable<any>
	{
		return this.http.get<Beer>(this.HOST + this.URI_BEERS, this.httpOptions);
	}
	
	/**
	*
	*
	*
	*
	**/
	getBeersByBar(bar: string) : Observable<any>
	{
		return this.http.get<Beer>(this.HOST + this.URI_BEER_ID + bar, this.httpOptions);
	}
		
	
	/**
	*
	*
	*
	**/
	getBeerForId(id: string) :  Observable<any>
	{
		return this.http.get<Beer>(this.HOST + this.URI_BEER_ID + id + this.GET, this.httpOptions);
	}
	
	/**
	*
	*
	*
	*
	**/
	beerInsert(data: string)
	{
		return this.http.post(this.HOST + this.URI_BEER_INSERT, JSON.stringify(data), this.httpOptions);
	}
	
		
	/**
	*
	*
	*
	**/
	beerUpdate(data: string) : Observable<any>
	{
		return this.http.put(this.HOST + this.URI_BEER_UPDATE, JSON.stringify(data), this.httpOptions);
	}
}
