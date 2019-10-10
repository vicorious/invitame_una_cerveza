export class Climate
{
	json : any;
	
	constructor(json : string)
	{
		this.json = json;
	}
	
	getJson()
	{
		return this.json;
	}		
	
}
