import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, map } from 'rxjs';

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

  async getTablesForGame(gameId: string): Promise<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const params = new HttpParams().set('gameId', gameId);

    try {
      const response = await this.http
        .get<any[]>(this.baseUrl + '/display_tables_for_game/', {
          headers,
          params,
        })
        .pipe(map((data) => Object.values(data)))
        .toPromise();

      return response;
    } catch (error) {
      // Obsługa błędu
      throw error;
    }
  }

  async checkIfFreeDate(
    gameId: string,
    startDate: string,
    endDate: string
  ): Promise<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    let params = { gameId, startDate, endDate };

    const response = await this.http
      .get<any[]>(this.baseUrl + '/check_if_free_date/', {
        headers,
        params,
      })
      .toPromise();

    return response;
  }

  createReservationsWithEmail(
    email: any,
    gameId: any,
    startDate: any,
    endDate: any,
    dishes: any,
    tables: any,
    peopleCount: any
  ) {
    return this.http.post<any>(this.baseUrl + '/create_reservation/', {
      email: email,
      gameId: gameId,
      startDate: startDate,
      endDate: endDate,
      dishes: dishes,
      tables: tables,
      peopleCount: peopleCount,
    });
  }
}
