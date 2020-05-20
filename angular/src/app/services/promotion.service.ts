import { Injectable } from '@angular/core';
import { Promotion } from '../dto/promotion';
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
export class PromotionService 
{
	public HOST                  : string = "http://localhost:5000"
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
	constructor(private http: HttpClient) { }
	
	/**
	*
	*
	*
	**/
	getPromotion()
	{
		let melas_doble_iipa = new Promotion("Melas doble IIPA", "assets/images/beer/melas/atomic_ipa.jpg", "Dulce y amarga cerveza con gran cantidad de alcohol para que en vez de saborearla; ALUCINES la cerveza", "10%");
		let milagrosa_ipa = new Promotion("IPA The pub", "assets/images/beer/milagrosa/ipa.jpg", "¡La mejor cerveceria de bogotá con cervezas artesanales del mundo!", "9%");
		let tommahowk_ipa = new Promotion("Tommahowk IPA", "assets/images/beer/tierra_santa/cervezas.jpg", "Tenemos todos los estilos de cerveza a todo tiempo y en todo lugar", "8%");	  
	  
		let promotions : Promotion[] = [melas_doble_iipa, milagrosa_ipa, tommahowk_ipa];
		return promotions;
	}
	
	/**
	*
	*
	*
	*
	**/
	getPromotions() : Observable<any>
	{
		return this.http.get(this.HOST + this.URI_PROMOTIONS, this.httpOptions).
		pipe
		(
			retry(1),
			catchError(CatchError.handleError)
		);
	}
	
		/**
	*
	*
	*
	*
	**/
	promotionInsert(data: string)
	{
		return this.http.post(this.HOST + this.URI_PROMOTIONS_INSERT, JSON.stringify(data), this.httpOptions).
		pipe
		(
			retry(1),
			catchError(CatchError.handleError)
		);
	}
	
		
	/**
	*
	*
	*
	**/
	promotionUpdate(data: string) : Observable<any>
	{
		return this.http.put(this.HOST + this.URI_PROMOTIONS_UPDATE, JSON.stringify(data), this.httpOptions).
		pipe
		(
			retry(1),
			catchError(CatchError.handleError)
		);
	}
		
}
