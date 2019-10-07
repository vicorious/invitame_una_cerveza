export class Bar
{
	name: string;
	image: string;
	direction: string;
	description: string;
	
	constructor(name: string, image: string, direction: string, description: string)
	{
		this.name = name;
		this.image = image;
		this.direction = direction;
		this.description = description;
	}
	
	getName()
	{
		return this.name;
	}
	
	getImage()
	{
		return this.image;
	}
	
	getDirection()
	{
		return this.direction;
	}
	
	getdescription()
	{
		return this.description;
	}
}
