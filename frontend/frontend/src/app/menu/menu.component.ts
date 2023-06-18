import { Component, OnInit } from '@angular/core';
import { MakingReservationService } from '../services/making-reservation.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css'],
})
export class MenuComponent implements OnInit {
  constructor(private db: MakingReservationService) {}

  dishList: any = [];

  ngOnInit(): void {
    this.refreshDishList();
  }

  refreshDishList() {
    this.db.getDishList().subscribe((data) => {
      this.dishList = Object.values(data)[0];
      console.log(this.dishList);
    });
  }

  refreshGamesList() {}
}
