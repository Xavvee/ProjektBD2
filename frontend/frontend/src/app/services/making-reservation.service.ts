import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
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
