import { Injectable } from '@angular/core';
import { Beer } from '../dto/beer';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError, Subject } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { of } from 'rxjs';
import { CatchError} from './catch-error';

@Injectable
(
	{
		providedIn: 'root'
	}
)
export class BeerService 
{
	public HOST            		: string = "http://localhost:5000"
	public BEER_PAIRING_URI     : string = "/beers/pairing/";
	
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

	private beer_subject = new Subject<Beer>();

	constructor(private http: HttpClient) { }

	beerMessage(_beer: Beer)
	{
		this.beer_subject.next(_beer);
	}

	beerClearMessage()
	{
		this.beer_subject.next();
	}

	beerGetMessage()
	{
		return this.beer_subject.asObservable();
	}

	getBeerPairing(beer_id)
	{
		return this.http.get<Beer>(this.HOST + this.BEER_PAIRING_URI + beer_id, this.httpOptions).
		pipe
		(
			retry(1),
			catchError(CatchError.handleError)
		);

	}

}
