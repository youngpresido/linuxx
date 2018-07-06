import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ScrumyuserService } from '../../scrumyuser.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
	isLoggedIn:boolean;
	loggedInUser:string;
	showRegister:boolean;
  constructor(
  	private auth:ScrumyuserService,
  	private route:Router,
  ) { }

  ngOnInit() {
  if(this.auth.getAuth() != null){
  this.auth.getAuth();
  this.isLoggedIn=true;
  this.loggedInUser="seun";
  }else{
  this.isLoggedIn=false;
  this.route.navigate(['login']);
  }
  console.log(this.auth.getAuth() != null);
  }
  onLogoutClick(){
  	localStorage.removeItem('token');
  	this.isLoggedIn=false;
  	alert("you have logged out");
  	this.route.navigate(['login']);
  }

}
