import { UserReservationsComponent } from './user-reservations/user-reservations.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { OfferComponent } from './offer/offer.component';
import { FoodOfferComponent } from './offer/food-offer/food-offer.component';

const routes: Routes = [
  { path: '', component: HomeComponent, pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'home', component: HomeComponent },
  { path: 'offer', component: OfferComponent },
  { path: 'my-reservations', component: UserReservationsComponent },
  { path: 'menu', component: FoodOfferComponent },
  { path: 'games', component: OfferComponent },
];

@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
