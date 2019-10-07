import { Injectable } from '@angular/core';
import { Beer } from '../dto/beer'

@Injectable

(
	{
		providedIn: 'root'
	}
)
export class BeersService 
{
  constructor() { }
  
  /**
  *
  *
  *
  *
  **/
  getBeersDummy(bar: string)
  {
	  let melas_doble_iipa = new Beer("Melas doble IIPA", "assets/images/beer/melas/atomic_ipa.jpg", "Dulce y amarga cerveza con gran cantidad de alcohol para que en vez de saborearla; ALUCINES la cerveza", "10%");
	  let milagrosa_ipa = new Beer("IPA The pub", "assets/images/beer/milagrosa/ipa.jpg", "¡La mejor cerveceria de bogotá con cervezas artesanales del mundo!", "9%");
	  let tommahowk_ipa = new Beer("Tommahowk IPA", "assets/images/beer/tierra_santa/cervezas.jpg", "Tenemos todos los estilos de cerveza a todo tiempo y en todo lugar", "8%");	  
	  let beer;
	  switch(bar)
	  {
		case "Melas":
			beer = melas_doble_iipa;
			break;
		case "The pub":
			beer = milagrosa_ipa;
			break;
		case "Tierra santa":
			beer = tommahowk_ipa;
			break;
		default:
			break;
	  }
			
		
	  let beers : Beer[] = [beer];
	  return beers;
  }
  
  
}
