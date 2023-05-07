import { Injectable, OnInit } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor() {}

  SignIn(email: string, password: string) {}

  SignUp(email: string, password: string, nick: string) {}

  SignOut() {}
}
