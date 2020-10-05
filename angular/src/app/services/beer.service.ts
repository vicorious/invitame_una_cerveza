import { Injectable } from '@angular/core';
import { Beer } from '../dto/beer';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError, Subject, ReplaySubject } from 'rxjs';
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

	private beer_subject = new ReplaySubject<any>(1);

	constructor(private http: HttpClient) { }

	beerMessage(message: any)
	{
		console.log(message)
		this.beer_subject.next(message);
	}

	beerClearMessage()
	{
		this.beer_subject.next();
	}

	beerGetMessage() : Observable<any>
	{
		return this.beer_subject.asObservable();
	}

	beerGetMessageSingle() : Subject<any>
	{
		return this.beer_subject;
	}

	getBeerPairing(beer_id)
	{
		return this.http.get<Beer>(this.HOST + this.BEER_PAIRING_URI + beer_id, this.httpOptions);

	}

}
