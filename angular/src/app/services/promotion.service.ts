import { Injectable } from '@angular/core';
import { Promotion } from '../dto/promotion';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';

@Injectable
(
	{
		providedIn: 'root'
	}
)
export class PromotionService 
{
	public HOST                  : string = "http://localhost:4200"
	public URI_PROMOTIONS        : string = "/promotions";
	public URI_PROMOTIONS_INSERT : string = "/promotion/INSERT";
	public URI_PROMOTIONS_UPDATE : string = "/promotion/UPDATE";
	
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
	constructor() { }
	
	/**
	*
	*
	*
	**/
	getPromotion()
	{
		let melas_doble_iipa = new Beer("Melas doble IIPA", "assets/images/beer/melas/atomic_ipa.jpg", "Dulce y amarga cerveza con gran cantidad de alcohol para que en vez de saborearla; ALUCINES la cerveza", "10%");
		let milagrosa_ipa = new Beer("IPA The pub", "assets/images/beer/milagrosa/ipa.jpg", "¡La mejor cerveceria de bogotá con cervezas artesanales del mundo!", "9%");
		let tommahowk_ipa = new Beer("Tommahowk IPA", "assets/images/beer/tierra_santa/cervezas.jpg", "Tenemos todos los estilos de cerveza a todo tiempo y en todo lugar", "8%");	  
	  
		let beers : Beer[] = [melas_doble_iipa, milagrosa_ipa, tommahowk_ipa];
		return beers;
	}
	
	/**
	*
	*
	*
	*
	**/
	getPromotions() : Observable<any>
	{
		return this.http.get(this.HOST + this.URI_PROMOTIONS, this.httpOptions).pipe(retry(1),catchError(this.errorHandl));
	}
	
		/**
	*
	*
	*
	*
	**/
	promotionInsert(data: string)
	{
		return this.http.post(this.HOST + this.URI_PROMOTIONS_INSERT, JSON.stringify(data), this.httpOptions).pipe(retry(1),catchError(this.errorHandl));
	}
	
		
	/**
	*
	*
	*
	**/
	promotionUpdate(data: string) : Observable<any>
	{
		return this.http.put(this.HOST + this.URI_PROMOTIONS_UPDATE, JSON.stringify(data), this.httpOptions).pipe(retry(1),catchError(this.errorHandl));
	}
}
