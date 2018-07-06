import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { ScrumyuserService } from '../../scrumyuser.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
	login;
  constructor(private scrumyUser:ScrumyuserService, public router:Router) { }

  ngOnInit() {
  this.login={
  username:"",
  password:""
  };
  }
  loginUser(){
      this.scrumyUser.loginUser(this.login)
      .subscribe(response=>{

        alert('User ' + this.login.username +' logged in');
        localStorage.setItem("token",response.token);
        this.router.navigate(['/']);
        console.log(response);
      },
    error=>{
    alert("login failed");
    console.log('error', error.message);
    this.router.navigate(['login']);
    
    }
  );

  
  }
}
