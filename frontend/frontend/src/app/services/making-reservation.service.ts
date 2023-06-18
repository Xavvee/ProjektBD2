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


  getReservationsByEmail(email: string): Observable<any[]> {
    return this.http.post<any[]>(this.baseUrl + '/find_reservation_by_param/', {email});
  }

  updateReservationStatus(email: string, id: string, status: string): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/update_reservation/`, {email: email ,reservationId: id, reservationStatus: status});
  }
  
  navigateToOrderDish(email: string, userId: string, reservationId: string): void {
    // Implement your navigation logic here...
  }
}
