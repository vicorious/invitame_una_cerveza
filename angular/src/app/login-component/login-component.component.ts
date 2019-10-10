import { Component, OnInit } from '@angular/core';
import { FacebookLoginProvider, GoogleLoginProvider } from "angularx-social-login";
import { AuthService } from "angularx-social-login";
import { SocialUser } from "angularx-social-login";

@Component({
  selector: 'app-login-component',
  templateUrl: './login-component.component.html',
  styleUrls: ['./login-component.component.css']
})
export class LoginComponentComponent implements OnInit 
{
	 
  private user: SocialUser;
  private loggedIn: boolean;

  constructor(private authService: AuthService) { }

  ngOnInit() 
  {
	this.authService.authState.subscribe
	(
		(user) => 
		{
			this.user = user;
			this.loggedIn = (user != null);
		}
	);
	  
  }
  
  signInWithGoogle(): void 
  {
		this.authService.signIn(GoogleLoginProvider.PROVIDER_ID);
  }
 
  signInWithFB(): void 
  {
		this.authService.signIn(FacebookLoginProvider.PROVIDER_ID);
  } 
 
  signOut(): void 
  {
		this.authService.signOut();
  }

}
