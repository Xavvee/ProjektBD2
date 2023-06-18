import { Component, OnInit } from '@angular/core';
import { MakingReservationService } from '../services/making-reservation.service';

@Component({
  selector: 'app-offer',
  templateUrl: './offer.component.html',
  styleUrls: ['./offer.component.css'],
})
export class OfferComponent implements OnInit {
  constructor(private db: MakingReservationService) {}

  gameList: any = [];
  reservationDate: Date = new Date();
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

  async getFreeDates(gameId: string) {
    try {
      const data = await this.db.getTablesForGame(gameId);
      this.tables = Object.values(data)[0];
      for (let table of this.tables) {
        console.log(table.reservedDates.length);
      }
      this.showTermDates = true;
    } catch (error) {
      // Obsługa błędu
      console.error(error);
    }
  }

  onDateChange(date: string) {
    this.reservationDate = new Date(date + 'T00:00:00Z');
    this.reservationDateStr = date;
    console.log(this.reservationDate);
  }

  ifReserved(term: any) {
    console.log(term);
    console.log(this.reservationDate);
    console.log(this.reservationDateStr);
    let newDate = new Date(term.startDate.$date);
    if (
      newDate.getFullYear() !== this.reservationDate.getFullYear() ||
      newDate.getMonth() !== this.reservationDate.getMonth() ||
      newDate.getDate() !== this.reservationDate.getDate()
    ) {
      return false;
    }
    return true;
  }

  checkIfReservationsExists(table: any) {
    console.log(table);
    if (table.reservedDates.length > 0) {
      return true;
    }
    return false;
  }
}
