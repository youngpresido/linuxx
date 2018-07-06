import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable,pipe,of,from,interval,merge,fromEvent } from 'rxjs';
import { ScrumyUser } from './modules/ScrumyUser';
import { map, filter, scan,tap} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ScrumyuserService {

  constructor(private http:HttpClient) { }

  registerUser(userData){
    return this.http.post('http://localhost:8000/register/', userData)
    .pipe(
        map(
          res=>localStorage.setItem('token',res["key"])
        )
    );
      
  }
  loginUser(userData):Observable<any>{
    console.log(userData);
    return this.http.post('http://127.0.0.1:8000/auth/', userData);
  }
  //check user status
  getAuth(){
  	return localStorage.getItem('token');
  }
}
