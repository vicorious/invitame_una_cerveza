import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-curioso-component',
  templateUrl: './curioso-component.component.html',
  styleUrls: ['./curioso-component.component.css']
})
export class CuriosoComponentComponent implements OnInit 
{
	public loading = false;

  constructor(private router: Router) { }

  ngOnInit() {}
  
  goBeerProfile()
  {
	  this.loading = true;
	  this.router.navigate(['/profile_beer']);
	  this.loading = false;
	  
  }
  

}
