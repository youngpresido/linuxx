import { Component, OnInit } from '@angular/core';
import { ScrumyuserService } from '../../scrumyuser.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-add-user',
  templateUrl: './add-user.component.html',
  styleUrls: ['./add-user.component.css'],
  providers:[ScrumyuserService]
})
export class AddUserComponent implements OnInit {

  data:any[];
  register;
  constructor(private scrumyUser:ScrumyuserService, public router:Router){

  }

  ngOnInit(){
    this.register={
      name:"",
      username:"",
      password1:"",
      email:"",
      role:"",
      password2:"",
    };

  }
  registerUser(){
    this.scrumyUser.registerUser(this.register).subscribe(user=>{
          alert("you are registered "+ user);
          this.router.navigate(['login']);  
      },error=>{
      alert(error.message);
      this.router.navigate(['add_user'])
    });
  }

}


