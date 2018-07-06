import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule,
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HTTP_INTERCEPTORS } from '@angular/common/http';
import { CustomHttpInterceptor } from './auth/interceptor';
import { RouterModule, Routes} from '@angular/router';
import { AppComponent } from './app.component';

import { ScrumyuserService } from './scrumyuser.service';
import { ScrumygoalserviceService  } from './scrumygoalservice.service';
//components import 
import { NavbarComponent } from './component/navbar/navbar.component';
import { HomeComponent } from './component/home/home.component';
import { AddUserComponent } from './component/add-user/add-user.component';
import { AddTaskComponent } from './component/add-task/add-task.component';
import { LoginComponent } from './component/login/login.component';
import { NavbarsComponent } from './component/navbars/navbars.component';
import { SidebarComponent } from './component/sidebar/sidebar.component';
import { ClientsComponent } from './component/clients/clients.component';
import { ClientDetailsComponent } from './component/client-details/client-details.component';
import { EditClientComponent } from './component/edit-client/edit-client.component';
import { PagenotfoundComponent } from './component/pagenotfound/pagenotfound.component';
import { DragulaModule } from 'ng2-dragula';

const appRoutes:Routes=[
  
  {path:'', component:HomeComponent},
  {path:'add_user', component:AddUserComponent},
  {path:'add_task', component:AddTaskComponent},
  {path:'test', component:SidebarComponent},
  {path:"login", component:LoginComponent}
];
@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    AddUserComponent,
    AddTaskComponent,
    LoginComponent,
    NavbarsComponent,
    SidebarComponent,
    ClientsComponent,
    ClientDetailsComponent,
    EditClientComponent,
    PagenotfoundComponent,
  ],
  imports: [
    DragulaModule,
    BrowserModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [
    ScrumyuserService,
    ScrumygoalserviceService,
    {
    provide:HTTP_INTERCEPTORS,
    useClass:CustomHttpInterceptor,
    multi:true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
