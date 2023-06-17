import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { User } from './models/user';
import { Roles } from './models/roles';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _userData = new BehaviorSubject<User | null>(null);
  public userData$: Observable<User | null> = this._userData.asObservable();

  constructor(private http: HttpClient, private router: Router) { }

  signIn(email: string, password: string) {
    return this.http.post<User>('/api/login', { email, password })
      .pipe(tap(user => {
        this._userData.next(user);
        this.router.navigate(['/home']);
      }));
  }

  signUp(email: string, password: string, nick: string) {
    return this.http.post<User>('/api/register', { email, password, nick })
      .pipe(tap(user => {
        this._userData.next(user);
        this.router.navigate(['/login']);
      }));
  }

  signOut() {
    this._userData.next(null);
    this.router.navigate(['/login']);
  }

  getRoles(userId: string) {
    return this.http.get<Roles>(`/api/users/${userId}/roles`);
  }
}
