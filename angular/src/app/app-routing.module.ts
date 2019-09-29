import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponentComponent } from './login-component/login-component.component';
import { BeerComponentComponent } from './beer-component/beer-component.component';
import { WeatherComponentComponent } from './weather-component/weather-component.component';
import { BarComponentComponent } from './bar-component/bar-component.component';
import { FooterComponentComponent } from './footer-component/footer-component.component';
import { BeersPluralComponentComponent } from './beers-plural-component/beers-plural-component.component';
import { ProfileComponentComponent } from './profile-component/profile-component.component';


const routes: Routes = 
[
  { path: 'home', component: BeerComponentComponent },
  { path: 'login', component: LoginComponentComponent },
  { path: 'climate', component: WeatherComponentComponent },
  { path: 'bar', component: BarComponentComponent },
  { path: 'footer', component: FooterComponentComponent },
  { path: 'beers', component: BeersPluralComponentComponent },
  { path: 'profile', component: ProfileComponentComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
