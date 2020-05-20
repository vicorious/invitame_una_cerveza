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
export class BeerService 
{
	constructor(private http: HttpClient) { }

}
