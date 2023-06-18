import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams  } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class MakingReservationService {
  baseUrl = 'http://127.0.0.1:8000/main';

  constructor(private http: HttpClient) {}

  getDishList(): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + '/find_all_dishes/');
  }

  getGamesList(): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + '/find_all_games/');
  }

  getReservationsByEmail(email: string): Observable<any[]> {
    return this.http.post<any[]>(this.baseUrl + '/find_reservation_by_param/', {
      email,
    });
  }

  updateReservationStatus(
    email: string,
    id: string,
    status: string
  ): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/update_reservation/`, {
      email: email,
      reservationId: id,
      reservationStatus: status,
    });
  }

  updateReservationDishes(
    email: string,
    reservationId: string,
    reservationDishList: string[]
  ) {
    return this.http.post<any>(`${this.baseUrl}/update_reservation/`, {
      email: email,
      reservationId: reservationId,
      dishes: reservationDishList,
    });
  }

  getReservationDishes(email: string, reservationId: string) {
    return this.http.post<any[]>(this.baseUrl + '/find_reservation_by_param/', {
      email,
      reservationId,
    });
  }

    getTablesForGame(gameId: string): Observable<any[]> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const params = new HttpParams().set('gameId', gameId);
    return this.http.get<any[]>(this.baseUrl + '/display_tables_for_game/', {
      headers,
      params,
    });
  }

  checkIfFreeDate(gameId: string, startDate: string, endDate: string) {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    let params = { gameId, startDate, endDate };
    return this.http.get<any[]>(this.baseUrl + '/check_if_free_date/', {
      headers,
      params,
    });
  }
}
