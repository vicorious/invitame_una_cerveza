import { Injectable } from '@angular/core';
import { Beer } from '../dto/beer';
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
export class BeerService 
{
	constructor() { }
}
