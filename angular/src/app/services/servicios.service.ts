import { Injectable } from '@angular/core';
//Componentes para el request
import {HttpClient} from "@angular/common/http";
import "rxjs/add/operator/map";
import {Observable} from "rxjs/Observable";

@Injectable
({
	
  providedIn: 'root'
  
})
export class ServiciosService 
{
	HOST					   				: string = 'http://127.0.0.1:5000';
	url_login								: string;
	url_registrame							: string;
	url_olvido_contrasena					: string;
	// Bares
	url_bar_por_id							: string;
	url_bares								: string;
	url_bares_insert						: string;
	url_bar_update							: string;
	// Cerveza
	url_cerveza_por_id						: string;
	url_cervezas							: string;
	url_cervezas_insert						: string;
	// Usuario Cerveza
	url_usuario_visitas_por_id				: string;
	url_usuario_visita_cerveza				: string;
	url_usuario_visita_cerveza_tipo_pago	: string;
	url_usuario_tipo_pago					: string;
	url_usuario_visitas_insert				: string;
	//Acompanamiento
	url_acompanamiento_insert				: string;
	url_acompanamientos						: string;
	url_acompanamiento_id					: string;
	url_acompanamiento_update				: string;
	//Manejo errores
	str_ejecucion_correcta					: string;
	str_ejecucion_erronea					: string;
	str_observable_correcto					: string;
	//Get´s
	
	
	constructor(private _http:HttpClient) 
	{
		this.url_login 									= this.HOST + "/login";
		this.url_registrame								= this.HOST + "/registrarse/INSERT";
		this.url_olvido_contrasena						= this.HOST + "/olvido_contrasena/UPDATE";
		this.url_bar_por_id								= this.HOST + "/bares/<bar_id>/GET";
		this.url_bares									= this.HOST + "/bares";
		this.url_bares_insert							= this.HOST + "/bares/INSERT";
		this.url_bar_update								= this.HOST + "/bares/UPDATE";
		this.url_cerveza_por_id							= this.HOST + "/cervezas/<_cerveza_id>/GET";
		this.url_cervezas								= this.HOST + "/cervezas/GET";
		this.url_cervezas_insert						= this.HOST + "/cerveza/INSERT";
		this.url_usuario_visitas_por_id					= this.HOST + "/usuario_visitas/<_usuario_id>/GET";
		this.url_usuario_visita_cerveza					= this.HOST + "/usuario_visitas/<_usuario_id>/GET/<_cerveza_id>/GET";
		this.url_usuario_visita_cerveza_tipo_pago		= this.HOST + "/usuario_visitas/<_usuario_id>/GET/<_cerveza_id>/GET/<tipo_pago_id>/GET";
		this.url_usuario_tipo_pago						= this.HOST + "/usuario_visitas/<_usuario_id>/GET/<tipo_pago_id>/GET";
		this.url_usuario_visitas_insert					= this.HOST + "/usuario_visitas/INSERT";
		this.url_acompanamiento_insert					= this.HOST + "/acompanamiento/INSERT";
		this.url_acompanamientos						= this.HOST + "/acompanamientos/GET";
		this.url_acompanamiento_id						= this.HOST + "/acompanamientos/<_acompanamiento_id>/GET";
		this.url_acompanamiento_update					= this.HOST + "/acompanamientos/UPDATE";
		
		this.str_ejecucion_correcta						= "? llamado correctamente: ";
		this.str_ejecucion_erronea						= "Llamada incorrecta (?), Por favor intentar de nuevo. ERROR: ";
		this.str_observable_correcto					= "El observable fue ejecutado correctamente (?)";
		
	}//Constructor
	
	/**
	*
	* LOGIN
	*
	*
	**/
	login(_json)
	{
		this._http.post(this.url_login,
		{
			_json
			
		}).subscribe
		(
			(val) => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Login"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Login"), response);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Login"));
			}
		);
		
	}//login
	
	/**
	*
	*
	* REGISTRARME
	*
	**/
	registrarme(_json)
	{
		this._http.post(this.url_registrame,
		{
			_json
			
		}).subscribe
		(
			(val) => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Registrarme"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Registrarme"), val);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Registrarme"));
			}
		);
		
	}//registrarme	
	
	/**
	*
	*
	* OLVIDO CONTRASENA
	*
	**/
	olvido_contrasena(_json):
	{
		const headers = new HttpHeaders().set("Content-Type", "application/json");

		this._http.put(this.url_olvido_contrasena,
		{
			_json
		},
			{headers}
		)
		.subscribe
		(
			val => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Olvido contrasena"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Olvido contrasena"), val);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Olvido contrasena"));
			}
		);
		
	}//olvido_contrasena
	
	// BARES	
	/**
	*
	*
	* BARES
	*
	**/
	bares():
	{
		this._http.get(this.url_bares)
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)
		
	}//bares
	
	/**
	*
	*
	* BAR POR ID
	*
	**/
	bar_por_id(_bar_id):

		this._http.get(this.url_bar_por_id.replace("<bar_id>",_bar_id))
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)
		
	}//bar_por_id
	
	
	/**
	*
	*
	* BAR INSERT
	*
	**/
	bar_insert(_json)
	{
		this._http.post(this.url_bares_insert,
		{
			_json
			
		}).subscribe
		(
			(val) => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Bar Insert"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Bar Insert"), val);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Bar Insert"));
			}
		);
		
	}//bar_insert	
	
	/**
	*
	*
	* BAR UPDATE
	*
	**/
	bar_update(_json):
	{
		const headers = new HttpHeaders().set("Content-Type", "application/json");

		this._http.put(this.url_bar_update,
		{
			_json
		},
			{headers}
		)
		.subscribe
		(
			val => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Bar update"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Bar update"), val);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Bar update"));
			}
		);
		
	}//bar_update	
	
	//CERVEZA
	
	/**
	*
	*
	* CERVEZAS
	*
	**/
	cervezas():
	{		
		this._http.get(this.url_cervezas)
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)		
		
	}//cervezas
	
	/**
	*
	*
	* CERVEZA POR ID
	*
	**/
	cerveza_id(_cerveza_id):
	{

		this._http.get(this.url_cerveza_por_id.replace("<cerveza_id>",_cerveza_id))
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)
		
	}//cerveza_id
	
	/**
	*
	*
	* CERVEZA INSERT
	*
	**/
	cerveza_insert(_json)
	{
		this._http.post(this.url_cervezas_insert,
		{
			_json
			
		}).subscribe
		(
			(val) => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Cerveza Insert"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Cerveza Insert"), val);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Cerveza Insert"));
			}
		);
		
	}//cerveza_insert

	//USUARIO CERVEZA
	
	/**
	*
	*
	* USUARIO VISITAS
	*
	**/
	usuario_visitas(_usuario_id):
	{		
		this._http.get(this.url_usuario_visitas_por_id.replace("<_usuario_id>",_usuario_id))
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)		
		
	}//usuario_visitas
	
	/**
	*
	*
	* USUARIO VISITAS CERVEZA
	*
	**/
	usuario_visitas_cerveza(_usuario_id, _cerveza_id):
	{		
		this._http.get(this.url_usuario_visita_cerveza.replace("<_usuario_id>",_usuario_id).replace("<_cerveza_id>",_cerveza_id))
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)		
		
	}//usuario_visitas_cerveza
	
	/**
	*
	*
	* USUARIO VISITAS CERVEZA TIPO_PAGO
	*
	**/
	usuario_visitas_cerveza_tipo_pago(_usuario_id, _cerveza_id, _tipo_pago_id):
	{		
		this._http.get(this.url_usuario_visita_cerveza_tipo_pago.replace("<_usuario_id>",_usuario_id).replace("<_cerveza_id>",_cerveza_id).replace("<_tipo_pago>",_tipo_pago_id));
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)		
		
	}//usuario_visitas_cerveza_tipo_pago	
		
	
	
	/**
	*
	*
	* USUARIO VISITAS TIPO_PAGO
	*
	**/
	usuario_tipo_pago(_usuario_id, _tipo_pago_id):
	{		
		this._http.get(this.url_usuario_tipo_pago.replace("<_usuario_id>",_usuario_id).replace("<_tipo_pago_id>",_tipo_pago_id));
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)		
		
	}//usuario_tipo_pago		
	
	/**
	*
	*
	* CERVEZA USUARIO INSERT
	*
	**/
	cerveza_usuario_insert(_json)
	{
		this._http.post(this.url_usuario_visitas_insert,
		{
			_json
			
		}).subscribe
		(
			(val) => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Cerveza Usuario Insert"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Cerveza Usuario Insert"), val);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Cerveza Usuario Insert"));
			}
		);
		
	}//cerveza_usuario_insert
	
	/**
	*
	*
	* ACOMPANAMIENTO INSERT
	*
	**/
	acompanamiento_insert(_json)
	{
		this._http.post(this.url_acompanamiento_insert,
		{
			_json
			
		}).subscribe
		(
			(val) => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Acompanamiento Insert"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Acompanamiento Insert"), val);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Acompanamiento Insert"));
			}
		);
		
	}//acompanamiento_insert

	/**
	*
	*
	* ACOMPANAMIENTOS
	*
	**/
	acompanamientos():
	{		
		this._http.get(this.url_acompanamientos)
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)		
		
	}//acompanamientos	
	
	/**
	*
	*
	* ACOMPANAMIENTOS ID
	*
	**/
	acompanamientos_id(_acompanamiento_id):
	{		
		this._http.get(this.url_acompanamiento_id.replace("<_acompanamiento_id>",_acompanamiento_id));
		.do
		(
			console.log
		)
		.map
		(
			data => 
			{
				_.values(data)
			}
		)		
		
	}//acompanamientos_id	
	
		/**
	*
	*
	* ACOMPANAMIENTO UPDATE
	*
	**/
	acompanamientos_update(_json):
	{
		const headers = new HttpHeaders().set("Content-Type", "application/json");

		this._http.put(this.url_acompanamiento_update,
		{
			_json
		},
			{headers}
		)
		.subscribe
		(
			val => 
			{
				console.log(this.str_ejecucion_correcta.replace("?","Acompanamiento update"), val);
			},
			response => 
			{
				console.log(this.str_ejecucion_erronea.replace("?","Acompanamiento update"), val);
			},
			() => 
			{
				console.log(this.str_observable_correcto.replace("?","Acompanamiento update"));
			}
		);
		
	}//acompanamientos_update	
	
	
  
}//NoBorrar
