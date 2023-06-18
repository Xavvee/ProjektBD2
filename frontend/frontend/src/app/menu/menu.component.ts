import { Component, OnInit } from '@angular/core';
import { MakingReservationService } from '../services/making-reservation.service';
import { FormGroup, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css'],
})
export class MenuComponent implements OnInit {
  constructor(private db: MakingReservationService) {}

  gameList: any = [];
  reservationDate: any | null = null;
  reservationDateStr: any | null = null;
  today!: string;
  maxDate!: string;
  showTermDates = false;
  tables: any = [];

  ngOnInit(): void {
    this.today = new Date().toISOString().split('T')[0];
    const maxDateObj = new Date();
    maxDateObj.setMonth(maxDateObj.getMonth() + 3);
    this.maxDate = maxDateObj.toISOString().split('T')[0];
    this.refreshGamesList();
  }

  refreshGamesList() {
    this.db.getGamesList().subscribe((data) => {
      this.gameList = Object.values(data)[0];
    });
  }

  getFreeDates(gameId: string) {
    this.db.getTablesForGame(gameId).subscribe((data) => {
      this.tables = Object.values(data)[0];
    });
    console.log(this.tables[0].reservedDates);
    this.showTermDates = true;
  }

  onDateChange(date: string) {
    this.reservationDate = new Date(date + 'T00:00:00Z');
    this.reservationDateStr = date;
    console.log(this.reservationDate);
  }

  ifReserved(term: any) {
    console.log(term.startDate.$date > this.reservationDate);
    if (term.startDate.$date > this.reservationDate) {
      return false;
    }
    return true;
  }
}
