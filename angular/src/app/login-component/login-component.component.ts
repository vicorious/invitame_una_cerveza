import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component
({
  selector: 'app-login-component',
  templateUrl: './login-component.component.html',
  styleUrls: ['./login-component.component.css']
})
export class LoginComponentComponent implements OnInit 
{
	 
  private user: SocialUser;
  private loggedIn: boolean;
  public loading = false;  

  constructor(private router: Router, private fire: AuthService) { }

  ngOnInit() {}
  
  signInWithTwitter(): void 
  {
	this.fire.signInWithTwitter();
  }
 
  signInWithFB(): void 
  {
		
  } 
 
  signOut(): void 
  {
		
  }
  
  singInWithOutSocialMedia(): void
  {
	  this.loading = true;
	  this.router.navigate(['/choose']);
	  this.loading = false;
  }

}
