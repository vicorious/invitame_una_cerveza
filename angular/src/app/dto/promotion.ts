export class Promotion
{
	name: string;
	image: string;
	abv: string;
	description: string;
	
	constructor(name: string, image: string, description: string, abv: string)
	{
		this.name = name;
		this.image = image;
		this.abv = abv;
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
	
	getDescription()
	{
		return this.description;
	}
	
	getAbv()
	{
		return this.abv;
	}
}