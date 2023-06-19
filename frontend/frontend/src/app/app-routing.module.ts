import { UserReservationsComponent } from './user-reservations/user-reservations.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { MenuComponent } from './menu/menu.component';
import { MenuAddToReservationComponent } from './menu-add-to-reservation/menu-add-to-reservation.component';
import { OfferComponent } from './offer/offer.component';
import { CreateUserComponent } from './create-user/create-user.component';


const routes: Routes = [
  { path: '', component: HomeComponent, pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'home', component: HomeComponent },
  { path: 'menu', component: MenuComponent},
  { path: 'my-reservations', component: UserReservationsComponent },
  { path: 'add-dish-to-reservation', component: MenuAddToReservationComponent},
  { path: 'offer', component: OfferComponent },
  { path: 'games', component: OfferComponent },
  { path: 'create-user', component: CreateUserComponent},
];

@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
