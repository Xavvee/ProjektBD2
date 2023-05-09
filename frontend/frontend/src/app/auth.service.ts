import { Injectable, OnInit } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor() {}

  SignIn(email: string, password: string) {
    //here some database magic happens
  }

  SignUp(email: string, password: string, nick: string) {
    //here some database magic happens
  }

  SignOut() {}
}
