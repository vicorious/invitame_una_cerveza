import { Injectable } from '@angular/core';
import { Promotion } from '../dto/promotion';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
<<<<<<< HEAD
import { of } from 'rxjs';
=======
>>>>>>> 627c1ec874e4949dcf63868c7d80a75920957b50

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
<<<<<<< HEAD
	constructor(private http: HttpClient) { }
=======
	constructor() { }
>>>>>>> 627c1ec874e4949dcf63868c7d80a75920957b50
	
	/**
	*
	*
	*
	**/
	getPromotion()
	{
<<<<<<< HEAD
		let melas_doble_iipa = new Promotion("Melas doble IIPA", "assets/images/beer/melas/atomic_ipa.jpg", "Dulce y amarga cerveza con gran cantidad de alcohol para que en vez de saborearla; ALUCINES la cerveza", "10%");
		let milagrosa_ipa = new Promotion("IPA The pub", "assets/images/beer/milagrosa/ipa.jpg", "¡La mejor cerveceria de bogotá con cervezas artesanales del mundo!", "9%");
		let tommahowk_ipa = new Promotion("Tommahowk IPA", "assets/images/beer/tierra_santa/cervezas.jpg", "Tenemos todos los estilos de cerveza a todo tiempo y en todo lugar", "8%");	  
	  
		let promotions : Promotion[] = [melas_doble_iipa, milagrosa_ipa, tommahowk_ipa];
		return promotions;
=======
		let melas_doble_iipa = new Beer("Melas doble IIPA", "assets/images/beer/melas/atomic_ipa.jpg", "Dulce y amarga cerveza con gran cantidad de alcohol para que en vez de saborearla; ALUCINES la cerveza", "10%");
		let milagrosa_ipa = new Beer("IPA The pub", "assets/images/beer/milagrosa/ipa.jpg", "¡La mejor cerveceria de bogotá con cervezas artesanales del mundo!", "9%");
		let tommahowk_ipa = new Beer("Tommahowk IPA", "assets/images/beer/tierra_santa/cervezas.jpg", "Tenemos todos los estilos de cerveza a todo tiempo y en todo lugar", "8%");	  
	  
		let beers : Beer[] = [melas_doble_iipa, milagrosa_ipa, tommahowk_ipa];
		return beers;
>>>>>>> 627c1ec874e4949dcf63868c7d80a75920957b50
	}
	
	/**
	*
	*
	*
	*
	**/
	getPromotions() : Observable<any>
	{
<<<<<<< HEAD
		return this.http.get(this.HOST + this.URI_PROMOTIONS, this.httpOptions).
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
=======
		return this.http.get(this.HOST + this.URI_PROMOTIONS, this.httpOptions).pipe(retry(1),catchError(this.errorHandl));
>>>>>>> 627c1ec874e4949dcf63868c7d80a75920957b50
	}
	
		/**
	*
	*
	*
	*
	**/
	promotionInsert(data: string)
	{
<<<<<<< HEAD
		return this.http.post(this.HOST + this.URI_PROMOTIONS_INSERT, JSON.stringify(data), this.httpOptions).
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
=======
		return this.http.post(this.HOST + this.URI_PROMOTIONS_INSERT, JSON.stringify(data), this.httpOptions).pipe(retry(1),catchError(this.errorHandl));
>>>>>>> 627c1ec874e4949dcf63868c7d80a75920957b50
	}
	
		
	/**
	*
	*
	*
	**/
	promotionUpdate(data: string) : Observable<any>
	{
<<<<<<< HEAD
		return this.http.put(this.HOST + this.URI_PROMOTIONS_UPDATE, JSON.stringify(data), this.httpOptions).
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
=======
		return this.http.put(this.HOST + this.URI_PROMOTIONS_UPDATE, JSON.stringify(data), this.httpOptions).pipe(retry(1),catchError(this.errorHandl));
>>>>>>> 627c1ec874e4949dcf63868c7d80a75920957b50
	}
}
