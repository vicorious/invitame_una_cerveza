import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http'; 
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';
import { NgxSpinnerModule } from "ngx-spinner";
// Firebase services + enviorment module
import { AngularFireModule } from "@angular/fire";
import { AngularFireAuthModule } from "@angular/fire/auth";
import { AngularFirestoreModule } from '@angular/fire/firestore';

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
import { environment } from '../environments/environment';
import { NotFoundComponent } from './not-found/not-found.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

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
    PromocionComponentComponent,
    NotFoundComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
	  HttpClientModule,
	  AppRoutingModule,
    AngularFireModule.initializeApp(environment.firebaseConfig),
    AngularFireAuthModule,
    AngularFirestoreModule,
    BrowserAnimationsModule,
    NgxSpinnerModule,
    ToastrModule.forRoot(),
    FontAwesomeModule
  ],
  providers: [BarService],
  bootstrap: [AppComponent]
})
export class AppModule { }
