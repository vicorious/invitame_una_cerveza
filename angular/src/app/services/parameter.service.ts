import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { retry } from 'rxjs/internal/operators/retry';
import { catchError } from 'rxjs/internal/operators/catchError';
import { CatchError } from './catch-error';

@Injectable({
  providedIn: 'root'
})
export class ParameterService 
{
  public HOST            		: string = "http://localhost:5000"
  public PAY_TYPE_URI       : string = "/pay_type";
  
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

  getPayType()
	{
		return this.http.get<any>(this.HOST + this.PAY_TYPE_URI, this.httpOptions);
	}

}
