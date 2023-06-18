import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
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

  // getTablesForGame(gameId): Observable<any[]> {
  //   return this.http.get<any[]>(this.baseUrl + '/display_tables_for_game/');
  // }
}
