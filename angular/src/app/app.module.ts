import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponentComponent } from './login-component/login-component.component';
import { BeerComponentComponent } from './beer-component/beer-component.component';
import { WeatherComponentComponent } from './weather-component/weather-component.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponentComponent,
    BeerComponentComponent,
    WeatherComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [BeerComponentComponent]
})
export class AppModule { }
