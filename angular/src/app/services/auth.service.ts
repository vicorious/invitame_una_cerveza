import { Injectable } from '@angular/core';
import { auth } from 'firebase/app';
import { AngularFireAuth } from "@angular/fire/auth";

@Injectable
(
	{
		providedIn: 'root'
	}
)
export class AuthService 
{
	constructor(public afAuth: AngularFireAuth) { }
  
  
	signInWithTwitter()
	{
		return this.AuthLogin(new auth.TwitterAuthProvider());
	}
  
	authLogin(provider) 
	{
		return this.afAuth.auth.signInWithPopup(provider).then
		(
			(result) => 
			{
				console.log('You have been successfully logged in!')
			}).catch((error) => 
			{
				console.log(error)
			})
	}
}
