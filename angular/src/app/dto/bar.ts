export class Bar
{
	name: string;
	imagen: string;
	direccion: string;
	descripcion: string;
	
	constructor(name: string, imagen: string, direccion: string, descripcion: string)
	{
		this.name = name;
		this.imagen = imagen;
		this.direccion = direccion;
		this.descripcion = descripcion;
	}
	
	getName()
	{
		return this.name;
	}
	
	getImage()
	{
		return this.imagen;
	}
	
	getDirection()
	{
		return this.direccion;
	}
	
	getDescripcion()
	{
		return this.descripcion;
	}
}
