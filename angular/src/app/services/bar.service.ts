import { Injectable } from '@angular/core';
import { Bar } from '../dto/bar'

@Injectable
(
	{
		providedIn: 'root'
	}
)
export class BarService 
{
  constructor() { }
  
  /**
  *
  * Get dummy bares
  *
  **/
  getDummyBar()
  {	  
	  let melas = new Bar("Melas","assets/images/melas.jpg", "CRA 11B # 71-16","La mejor IPA de bogotá se encuentra aqui. ¡Y SE LLAMA ATOMIC IPA!");
	  let thepub = new Bar("The pub", "assets/images/the_pub.jpg", "CALLE 71B # 10-36", "The pub, el lugar donde encontraras todas las cervezas que puedan existir. !Animate!");
	  let tierrasanta = new Bar("Tierra santa", "assets/images/tierra_santa.jpg", "CRA 11 # 71-75", "Tenemos todos los estilos de cerveza a todo tiempo y en todo lugar");
	  
	  let bares: Bar[] = [melas, thepub, tierrasanta];
	  
	  return bares;	  
  }
  
}
