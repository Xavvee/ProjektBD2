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
  userDate: any = new Date();
  userDateStr: any | null = null;
  userReservationHoursStart: any = '12:00';
  userReservationHoursEnd: any = '13:00';
  today!: string;
  maxDate!: string;
  showTermDates = false;
  tables: any = [];
  ifFreeTermin!: any;
  userEmail!: string;
  selectedGameId!: string;

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
      this.showTermDates = true;
    } catch (error) {
      console.error(error);
    }
  }

  onDateChange(date: string) {
    this.reservationDate = new Date(date + 'T00:00:00Z');
    this.reservationDateStr = date;
    console.log(this.reservationDate);
  }

  ifReserved(term: any) {
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

  userDateChange(date: string) {
    this.userDate = new Date(date + 'T00:00:00Z');
    this.userDateStr = date;
  }

  checkTermin() {
    this.ifFreeTermin = true;
  }

  convertDate(dateString: string) {
    const date = new Date(dateString);

    const year = date.getUTCFullYear();
    const month = (date.getUTCMonth() + 1).toString().padStart(2, '0'); // Miesiące w obiekcie Date są indeksowane od 0, dlatego dodajemy 1
    const day = date.getUTCDate();
    const hours = date.getUTCHours();
    const minutes = date.getUTCMinutes();
    const seconds = date.getUTCSeconds();

    const transformedDate = `${year}-${month}-${day
      .toString()
      .padStart(2, '0')}T${hours.toString().padStart(2, '0')}:${minutes
      .toString()
      .padStart(2, '0')}:${seconds.toString().padStart(2, '0')}Z`;

    console.log(transformedDate); // Wynik: 2023-06-20T02:00:00Z
    return transformedDate;
  }

  addHoursToDate(dateString: any, hourString: any) {
    const date = new Date(dateString);

    // Pobieranie godziny i minut z łańcucha znaków godziny
    const [hour, minute] = hourString.split(':');

    // Ustawianie nowej godziny w obiekcie Date
    date.setUTCHours(hour);
    date.setUTCMinutes(minute);

    // Formatowanie daty i czasu do żądanego formatu
    const year = date.getUTCFullYear();
    const month = (date.getUTCMonth() + 1).toString().padStart(2, '0');
    const day = date.getUTCDate().toString().padStart(2, '0');
    const formattedTime = `${hour}:${minute}:00Z`;
    const transformedDate = `${year}-${month}-${day}T${formattedTime}`;

    console.log(transformedDate); // Wynik: 2023-06-23T12:00:00Z
    return transformedDate;
  }

  checkTimeRange(start: any, end: any) {
    const startTime = new Date(`2000-01-01T${start}:00Z`);
    const endTime = new Date(`2000-01-01T${end}:00Z`);
    const time10AM = new Date(`2000-01-01T10:00:00Z`);
    const time2AM = new Date(`2000-01-02T02:00:00Z`);

    return endTime > startTime && startTime > time10AM && endTime < time2AM;
  }

  makeReservation() {
    console.log(this.userDate);
    let newDate = this.convertDate(this.userDate);
    console.log(this.userReservationHoursStart);
    console.log(this.userReservationHoursEnd);
    if (
      !this.checkTimeRange(
        this.userReservationHoursStart,
        this.userReservationHoursEnd
      )
    ) {
      throw console.error('The hour range is wrong, 10:00<start<end<02:00');
    }
    let start = this.addHoursToDate(newDate, this.userReservationHoursStart);
    let end = this.addHoursToDate(newDate, this.userReservationHoursEnd);
    console.log(this.userEmail);
    console.log(this.selectedGameId);
    //tutaj wołam dodaj rezerwację z tymi danymi którymi mam i essa
  }
}
