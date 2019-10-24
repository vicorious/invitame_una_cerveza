import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile-component',
  templateUrl: './profile-component.component.html',
  styleUrls: ['./profile-component.component.css']
})
export class ProfileComponentComponent implements OnInit 
{
	public loading = false;	

  constructor() { }

  ngOnInit() 
  {
	  this.loading = true;
	  this.loading = false;
  }

}
