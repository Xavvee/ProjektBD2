import { Component } from '@angular/core';
import { MakingReservationService } from '../services/making-reservation.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-create-user',
  templateUrl: './create-user.component.html',
  styleUrls: ['./create-user.component.css'],
})
export class CreateUserComponent {
  user = {
    firstName: '',
    lastName: '',
    dateOfBirth: '',
    email: '',
    phone: '',
    address: ''
    // ... add other user properties here
  };

  constructor(
    private reservationService: MakingReservationService,
    private router: Router
  ) {}

  onSubmit(): void {
    this.reservationService.createUser(this.user).subscribe(
      () => this.router.navigate(['/my-reservations'], { queryParams: { email: this.user.email }}),
      error => console.error('There was an error while creating the user', error)
    );
  }
}

