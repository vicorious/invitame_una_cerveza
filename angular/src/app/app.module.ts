import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponentComponent } from './login-component/login-component.component';
import { BeerComponentComponent } from './beer-component/beer-component.component';
import { WeatherComponentComponent } from './weather-component/weather-component.component';
import { BarComponentComponent } from './bar-component/bar-component.component';
import { FooterComponentComponent } from './footer-component/footer-component.component';
import { BeersPluralComponentComponent } from './beers-plural-component/beers-plural-component.component';
import { ProfileComponentComponent } from './profile-component/profile-component.component';
import { CodigoComponentComponent } from './codigo-component/codigo-component.component';
import { ReclamaCodigoComponentComponent } from './reclama-codigo-component/reclama-codigo-component.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponentComponent,
    BeerComponentComponent,
    WeatherComponentComponent,
    BarComponentComponent,
    FooterComponentComponent,
    BeersPluralComponentComponent,
    ProfileComponentComponent,
    CodigoComponentComponent,
    ReclamaCodigoComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [ReclamaCodigoComponentComponent]
})
export class AppModule { }
