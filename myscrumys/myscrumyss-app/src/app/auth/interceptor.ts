import { Observable } from 'rxjs';
import { Location } from '@angular/common';
import { Injectable, Injector } from '@angular/core';
import { HttpInterceptor } from '@angular/common/http';
import { HttpRequest } from '@angular/common/http';
import { HttpHandler } from '@angular/common/http';
import { HttpEvent } from '@angular/common/http';
import { ScrumygoalserviceService } from '../scrumygoalservice.service';
import { HttpHeaders } from '@angular/common/http';
import {from} from'rxjs';
 
@Injectable()
export class CustomHttpInterceptor implements HttpInterceptor {
  constructor(private msalService: ScrumygoalserviceService) {}
  
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    return from(this.handleAccess(request, next));
    //console.log("this is intercepted");
  }
 
  private async handleAccess(request: HttpRequest<any>, next: HttpHandler):
      Promise<HttpEvent<any>> {
    const token = await this.msalService.getToken();
    let changedRequest = request;
    // HttpHeader object immutable - copy values
    const headerSettings: {[name: string]: string | string[]; } = {};
 
    for (const key of request.headers.keys()) {
      headerSettings[key] = request.headers.getAll(key);
    }
    if (token) {
      headerSettings['Authorization'] = 'token ' + token;
    }
    headerSettings['Content-Type'] = 'application/json';
    const newHeader = new HttpHeaders(headerSettings);
 
    changedRequest = request.clone({
      headers: newHeader});
    return next.handle(changedRequest).toPromise();
  }
 
}