import { Injectable } from '@angular/core';
import { Bar } from '../dto/bar'
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { of } from 'rxjs';

@Injectable
(
	{
		providedIn: 'root'
	}
)
export class BarService 
{
	
	public HOST           : string = "http://localhost:4200"
	public URI_BARS       : string = "/bars";
	public URI_BAR_ID     : string = "/bar/";
	public GET            : string = "/GET";
	public URI_BAR_INSERT : string = "/bar/INSERT";
	public URI_BAR_UPDATE : string = "/bar/UPDATE";
	
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
	* Get dummy bares
	*
	**/
	getDummyBar()
	{	  
		let melas = new Bar("Melas","assets/images/melas.jpg", "CRA 11B # 71-16","La mejor IPA de bogotá se encuentra aqui. ¡Y SE LLAMA ATOMIC IPA!");
		let thepub = new Bar("The pub", "assets/images/the_pub.jpg", "CALLE 71B # 10-36", "The pub, el lugar donde encontraras todas las cervezas que puedan existir. !Animate!");
		let tierrasanta = new Bar("Tierra santa", "assets/images/tierra_santa.jpg", "CRA 11 # 71-75", "Tenemos todos los estilos de cerveza a todo tiempo y en todo lugar");
	  
		let bares: Bar[] = [melas, thepub, tierrasanta];
	  
		return bares;	  
	}
	
	/**
	*
	*
	*
	**/
	getBars() : Observable<any>
	{
		return this.http.get(this.HOST + this.URI_BARS, this.httpOptions)
		.pipe
		(
			retry(1),
			catchError
			(
				error => 
				{
					console.error('Pailander el servicio');
					return of({results: {}});
				}
			)
		);
		
	}
	
	/**
	*
	*
	*
	**/
	getBarForId(id: number) : Observable<any>
	{
		return this.http.get(this.HOST + this.URI_BAR_ID + id + this.GET, this.httpOptions).
		pipe
		(
			retry(1),
			catchError
			(
				error => 
				{
					return of({results: null});
				}
			)
		);
	}
	
	/**
	*
	*
	*
	**/
	insertBar(data: string) : Observable<any>
	{
		return this.http.post(this.HOST + this.URI_BAR_INSERT, JSON.stringify(data), this.httpOptions).
		pipe
		(
			retry(1),
			catchError
			(
				error => 
				{
					return of({results: null});
				}
			)
		);
	}
	
	
	/**
	*
	*
	*
	**/
	updateBar(data: string) : Observable<any>
	{
		return this.http.put(this.HOST + this.URI_BAR_UPDATE, JSON.stringify(data), this.httpOptions).
		pipe
		(
			retry(1),
			catchError
			(
				error => 
				{
					return of({results: null});
				}
			)
		);
	}
	
  
}
