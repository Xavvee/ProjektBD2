import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './home/header/header.component';
import { MenuComponent } from './menu/menu.component';
import { OfferNavBarComponent } from './menu/offer-nav-bar/offer-nav-bar.component';
import { UserReservationsComponent } from './user-reservations/user-reservations.component';
import { FoodOfferComponent } from './menu/food-offer/food-offer.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    LoginComponent,
    NavBarComponent,
    HomeComponent,
    HeaderComponent,
    MenuComponent,
    OfferNavBarComponent,
    UserReservationsComponent,
    FoodOfferComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
