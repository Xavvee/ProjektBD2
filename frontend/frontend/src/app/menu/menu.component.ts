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
  filteredDishes: any = [];
  selectedType: string = '';
  searchTerm: string = '';
  minValue: number = 20;
  maxValue: number = 80;
  dishTypes: string[] = [];

  ngOnInit(): void {
    this.refreshDishList();
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
}
