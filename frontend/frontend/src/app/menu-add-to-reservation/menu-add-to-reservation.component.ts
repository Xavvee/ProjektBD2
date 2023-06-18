import { Component, OnInit } from '@angular/core';
import { MakingReservationService } from '../services/making-reservation.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Dish } from '../models/dish';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'app-menu-add-to-reservation',
  templateUrl: './menu-add-to-reservation.component.html',
  styleUrls: ['./menu-add-to-reservation.component.css'],
})
export class MenuAddToReservationComponent implements OnInit {
  constructor(
    private db: MakingReservationService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  reservationDishList: Dish[] = [];
  dishList: any = [];
  filteredDishes: any = [];
  selectedType: string = '';
  searchTerm: string = '';
  minValue: number = 20;
  maxValue: number = 80;
  dishTypes: string[] = [];
  email: string = '';
  reservationId: string = '';

  ngOnInit(): void {
    this.route.queryParams.subscribe((params) => {
      this.email = params['email'];
      this.reservationId = params['reservationId'];
    });
    this.refreshDishList();
    this.fetchOrderedDishes();
  }

  fetchOrderedDishes(): void {
    this.db
      .getReservationDishes(this.email, this.reservationId)
      .pipe(tap((data: any) => console.log(data)))
      .subscribe((data) => {
        if (data.length > 0) {
          let dataUnpacked: any = data[0];
          if (
            dataUnpacked.orders &&
            dataUnpacked.orders.length > 0 &&
            dataUnpacked.orders[0].dishes
          ) {
            this.reservationDishList = dataUnpacked.orders[0].dishes.map(
              (dish: any) => new Dish(dish.dishId, dish.description)
            );
          }
        }
      });
  }
  refreshDishList(): void {
    this.db.getDishList().subscribe((data) => {
      this.dishList = Object.values(data)[0];
      this.filteredDishes = Object.values(data)[0];
      this.extractDishTypes();
      this.minValue = this.getMinPrice();
      this.maxValue = this.getMaxPrice();
      this.filterDishes();
    });
  }

  extractDishTypes(): void {
    this.dishTypes = Array.from(
      new Set(this.dishList.map((item: any) => item.dishType))
    );
  }

  filterDishes(): void {
    let filteredDishes = this.dishList;

    if (this.selectedType) {
      filteredDishes = filteredDishes.filter(
        (item: any) => item.dishType === this.selectedType
      );
    }

    if (this.searchTerm) {
      filteredDishes = filteredDishes.filter((item: any) =>
        item.description.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    }

    filteredDishes = filteredDishes.filter(
      (item: any) =>
        parseFloat(item.dishPrice) >= this.minValue &&
        parseFloat(item.dishPrice) <= this.maxValue
    );

    this.filteredDishes = filteredDishes;
  }

  getMinPrice(): number {
    return Math.min(
      ...this.dishList.map((item: any) => parseFloat(item.dishPrice))
    );
  }

  getMaxPrice(): number {
    return Math.max(
      ...this.dishList.map((item: any) => parseFloat(item.dishPrice))
    );
  }

  addDish(dishId: string, dishType: string): void {
    this.reservationDishList.push(new Dish(dishId, dishType));
  }

  removeDish(dishId?: string) {
    if (dishId) {
      const dishIndex = this.reservationDishList.findIndex(
        (dish) => dish.dishId === dishId
      );
      if (dishIndex > -1) {
        this.reservationDishList.splice(dishIndex, 1);
      }
    }
  }

  isDishInReservation(dishId?: string): boolean {
    if (dishId && this.reservationDishList) {
      return this.reservationDishList.some((dish) => dish.dishId === dishId);
    }
    return false;
  }

  makeOrder(email: string): void {
    const dishIds = this.reservationDishList.map((dish) => dish.dishId);
    this.db
      .updateReservationDishes(this.email, this.reservationId, dishIds)
      .subscribe(() => {
        this.router.navigate(['/my-reservations'], {
          queryParams: { email },
        });
      });
  }
}
