import { Injectable } from '@angular/core';
import { Beer } from '../dto/beer'

@Injectable
(
	{
		providedIn: 'root'
	}
)
export class PromotionService 
{
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
}
