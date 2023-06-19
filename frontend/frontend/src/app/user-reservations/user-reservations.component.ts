import { Component, OnInit } from '@angular/core';
import { MakingReservationService } from '../services/making-reservation.service';
import { ActivatedRoute, Router } from '@angular/router';
import { DatePipe } from '@angular/common';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-user-reservations',
  templateUrl: './user-reservations.component.html',
  styleUrls: ['./user-reservations.component.css'],
  providers: [DatePipe],
})
export class UserReservationsComponent implements OnInit {
  reservations: any[] = [];
  currentDate: Date;
  userEmail: string = '';
  expandedIndex: number | null = null;
  filteredReservations: any[] = [];
  showOldReservations: boolean = false;

  constructor(
    private reservationService: MakingReservationService,
    private route: ActivatedRoute,
    private router: Router,
    private datePipe: DatePipe
  ) {
    this.currentDate = new Date();
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe((params) => {
      this.userEmail = params['email'];
    });
    if (this.userEmail != null) {
      this.fetchReservations();
    }
  }

  fetchReservations(): void {
    this.reservationService.getReservationsByEmail(this.userEmail).subscribe(
      (data) => {
        this.reservations = data;
        this.filterReservations();
      },
      (error: HttpErrorResponse) => {
        console.error(error);
        if (error.status === 404) {
          this.router.navigateByUrl('/create-user');
        }
      }
    );
  }

  createUser(): void {
    const userData = {
      email: this.userEmail,
    };

    this.reservationService.createUser(userData).subscribe(
      (response) => {
        console.log('User created successfully', response);
        this.router.navigate(['/create-user']);
      },
      (error) =>
        console.error('There was an error while creating the user', error)
    );
  }

  onAddDishes(email: string, reservationId: string) {
    this.router.navigate(['/add-dish-to-reservation'], {
      queryParams: { email, reservationId },
    });
  }

  onCancel(id: string): void {
    this.reservationService
      .updateReservationStatus(this.userEmail, id, 'Canceled')
      .subscribe(() => this.fetchReservations());
  }

  onPay(id: string): void {
    this.reservationService
      .updateReservationStatus(this.userEmail, id, 'Confirmed')
      .subscribe(() => this.fetchReservations());
  }

  isFutureDate(dateString: string): boolean {
    const date = new Date(dateString);
    return date.getTime() > this.currentDate.getTime();
  }

  calculateTotalPrice(reservation: any): number {
    let hoursDifference =
      Math.abs(
        new Date(reservation.endDate).getTime() -
          new Date(reservation.startDate).getTime()
      ) / 3600000;
    let gamesPrice = 0;
    if (reservation.games && reservation.games.length > 0) {
      gamesPrice = Number(reservation.games[0].pricePerHour) * hoursDifference;
    }
    let finalPrice = 0;
    if (reservation.orders && reservation.orders.length > 0) {
      finalPrice = Number(reservation.orders[0].finalPrice);
    }
    let result: number = gamesPrice + finalPrice;
    return result;
  }

  getOrderedDishes(reservation: any): string {
    let dishes: string[] = [];
    if (
      reservation.orders &&
      reservation.orders.length > 0 &&
      reservation.orders[0].dishes
    ) {
      for (let dish of reservation.orders[0].dishes) {
        dishes.push(dish.dishType);
      }
    }

    return dishes.join(', ');
  }

  transformDate(date: string): string {
    return this.datePipe.transform(date, 'dd-MM-yyyy, hh:mm a')!;
  }

  // New method to filter reservations
  filterReservations(): void {
    this.filteredReservations = this.reservations.filter(
      (reservation) =>
        this.isFutureDate(reservation.startDate) || this.showOldReservations
    );
  }

  // New method to toggle old reservations
  toggleOldReservations(): void {
    this.showOldReservations = !this.showOldReservations;
    this.filterReservations(); // Refilter the reservations when we toggle old reservations
  }
}
