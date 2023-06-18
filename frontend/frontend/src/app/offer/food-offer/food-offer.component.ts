import { Component, OnInit } from '@angular/core';
import { MakingReservationService } from '../../services/making-reservation.service';

@Component({
  selector: 'app-food-offer',
  templateUrl: './food-offer.component.html',
  styleUrls: ['./food-offer.component.css'],
})
export class FoodOfferComponent implements OnInit {
  constructor(private db: MakingReservationService) {}

  dishList: any = [];

  ngOnInit(): void {
    this.refreshDishList();
  }

  refreshDishList() {
    this.db.getDishList().subscribe((data) => {
      this.dishList = Object.values(data)[0];
    });
  }
}
