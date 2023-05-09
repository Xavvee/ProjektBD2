import { AuthService } from '../auth.service';
import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, FormControl, Validators} from '@angular/forms'
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {

  constructor(private authService: AuthService, private formBuilder: FormBuilder, private router: Router) {}

  loginForm!: FormGroup
  email!: string
  password!: string

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group ({
      email: [''],
      password: ['']
    })
  }

  logIn() {
    this.newUser()
    this.authService.SignIn(this.email, this.password)
  }

  newUser() {
    this.email = this.loginForm.get('email')!.value
    this.password = this.loginForm.get('password')!.value
  }

  reloadAll() {
    this.router.navigateByUrl('/',{skipLocationChange:true}).then(()=>{
      this.router.navigate(['']).then(()=>{
        window.location.reload
      })
    })
  }
}
