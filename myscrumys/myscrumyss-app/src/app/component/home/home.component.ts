import { Component, OnInit } from '@angular/core';
import { ScrumygoalserviceService } from '../../scrumygoalservice.service';
import { ScrumyuserService } from '../../scrumyuser.service';
import { DragulaService } from 'ng2-dragula';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
	scrumygoals;
  isEdit:boolean=false;
  constructor(public scrumygoalservice:ScrumygoalserviceService, private dragulaService: DragulaService) {

dragulaService.drag.subscribe((value) => {
      console.log(`drag: ${value[0]}`);
      this.onDrag(value.slice(1));
    });
    dragulaService.drop.subscribe((value) => {
      console.log(`drop: ${value[0]}`);
      this.onDrop(value.slice(1));
    });
    dragulaService.over.subscribe((value) => {
      console.log(`over: ${value[0]}`);
      this.onOver(value.slice(1));
    });
    dragulaService.out.subscribe((value) => {
      console.log(`out: ${value[0]}`);
      this.onOut(value.slice(1));
    });

  }

  ngOnInit() {
  this.scrumygoalservice.getData().subscribe(goals=>{
      this.scrumygoals=goals;
      console.log(goals);
    }, error=>{
      console.log("errors",error);
    });
  }
  onDelete(id){
    this.scrumygoalservice.deleteStatus(id).subscribe(res=>{
        for(let i=0; i<this.scrumygoals.length; i++){
          if(this.scrumygoals[i].id==id){
            this.scrumygoals.splice(i,1);
          }
        }

    });
  }
  private onDrag(args) {
    let [e, el] = args;
    // do something
  }
  
  private onDrop(args) {
    let [e, el] = args;
    // do something
  }
  
  private onOver(args) {
    let [e, el, container] = args;
    // do something
  }
  
  private onOut(args) {
    let [e, el, container] = args;
    // do something
  }
    onUpdate(goals){
      //this.isEdit=true;
      //this.scrumygoals=goals;

      this.scrumygoalservice.updateGoals(this.scrumygoals).subscribe(goals=>{
          for(let i=0; i<this.scrumygoals.length; i++){
          if(this.scrumygoals[i].id==this.scrumygoals.id){
            this.scrumygoals.splice(i,1);
          }
        }
        this.scrumygoals.unshift(goals);        
      });
    }
  }


