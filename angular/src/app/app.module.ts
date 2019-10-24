import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgxLoadingModule } from 'ngx-loading';
import { HttpClientModule } from '@angular/common/http'; 

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
import { EleccionComponentComponent } from './eleccion-component/eleccion-component.component';
import { CuriosoComponentComponent } from './curioso-component/curioso-component.component';
import { PromocionComponentComponent } from './promocion-component/promocion-component.component';
import { BarService } from './services/bar.service';

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
    ReclamaCodigoComponentComponent,
    EleccionComponentComponent,
    CuriosoComponentComponent,
    PromocionComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
	NgxLoadingModule.forRoot({}),
	HttpClientModule
  ],
  providers: [BarService],
  bootstrap: [AppComponent]
})
export class AppModule { }
