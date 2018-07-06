import { Injectable, Injector } from '@angular/core';
import { Observable } from 'rxjs';
import { map, filter, scan } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Http, Headers, Response } from '@angular/http';
//import decode from 'jwt-decode';
@Injectable({
  providedIn: 'root',
})
export class ScrumygoalserviceService {

scrumygoals:Observable<any[]>;
  constructor(public http:HttpClient) { }
  



  addTask(userData):Observable<any>{
  console.log(userData);
    return this.http.post('http://127.0.0.1:8000/scrumygoals/', userData);
  }

 public getToken(){
  return localStorage.getItem('token');
}
public isAuthenticated():boolean{
	const token=this.getToken();
	if(token){
		return true
	}else{
	//return tokenNotExpired(null,token);
	return false;
	}
}
  getData(){
  const options={
  headers:new HttpHeaders({
  	"Content-Type":'application/json',
  	"Authorization":`token "${this.getToken()}"`
  })
  }
  	console.log(`Bearer "${this.getToken()}"`);
  	return this.http.get("http://localhost:8000/scrumyusers/");

  }

  getStatus(){
    return this.http.get("http://localhost:8000/goalstatus/");  
  }
  deleteStatus(id){
    return this.http.delete("http://127.0.0.1:8000/scrumygoals/"+id);
  }
  updateGoals(scrumygoals){
    return this.http.put("http://127.0.0.1:8000/scrumygoals/"+scrumygoals.id,scrumygoals);
  }
}
