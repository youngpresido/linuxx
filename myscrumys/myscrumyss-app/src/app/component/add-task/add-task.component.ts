import { Component, OnInit } from '@angular/core';
import { ScrumygoalserviceService } from '../../scrumygoalservice.service';
import { Router } from "@angular/router";
@Component({
  selector: 'app-add-task',
  templateUrl: './add-task.component.html',
  styleUrls: ['./add-task.component.css']
})
export class AddTaskComponent implements OnInit {
	goal;
  allstatus;
  constructor(private scrumyGoals:ScrumygoalserviceService, public router:Router) { 


console.log(this.allstatus);

  }

  ngOnInit() {
  this.goal={
  	task:"",
  	status:"",
  	title:"",

  }
this.scrumyGoals.getStatus().subscribe(goals=>{
      this.allstatus=goals;
      console.log(this.allstatus);
    }, error=>{
      console.log("errors",error);
    });

  

  }
  

   

  addTask({value,valid}){
    if(!valid){
      alert("Fill in all fields");
      this.router.navigate(['add_task']);
  }
  else{
  console.log(value);
  this.scrumyGoals.addTask(value).subscribe(user=>{
          alert("Task added  "+ user);
          this.router.navigate(['/']);  
      },error=>{
      alert(error.message);
  this.router.navigate(['add_task']);
    

      }
  )
  
}
}
}