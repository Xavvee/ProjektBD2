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
  selectedPrice: [number, number] = [0, 100]; 
  dishTypes: string[] = [];

  ngOnInit(): void {
    this.refreshDishList();
  }

  refreshDishList(): void {
    this.db.getDishList().subscribe((data) => {
      this.dishList = Object.values(data)[0];
      this.filteredDishes = Object.values(data)[0];
      this.extractDishTypes();
      this.selectedPrice = [this.getMinPrice(), this.getMaxPrice()]; 
      this.filterDishes();
    });
  }

  extractDishTypes(): void {
    this.dishTypes = Array.from(new Set(this.dishList.map((item: any) => item.dishType)));
  }

  filterDishes(): void {
    let filteredDishes = this.dishList;
  
    if (this.selectedType) {
      filteredDishes = filteredDishes.filter((item: any) => item.dishType === this.selectedType);
    }
  
    if (this.searchTerm) {
      filteredDishes = filteredDishes.filter(
      (item: any) =>
        item.description.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    }
  
    filteredDishes = filteredDishes.filter(
      (item: any) =>
        parseFloat(item.dishPrice) >= this.selectedPrice[0] &&
        parseFloat(item.dishPrice) <= this.selectedPrice[1]
    );
  
    this.filteredDishes = filteredDishes;
  }
  

  getMinPrice(): number {
    return Math.min(...this.dishList.map((item: any) => parseFloat(item.dishPrice)));
  }

  getMaxPrice(): number {
    return Math.max(...this.dishList.map((item: any) => parseFloat(item.dishPrice)));
  }
}