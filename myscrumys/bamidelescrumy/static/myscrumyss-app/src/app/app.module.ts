import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes} from '@angular/router';
import { AppComponent } from './app.component';
import { NavbarComponent } from './component/navbar/navbar.component';
import { HomeComponent } from './component/home/home.component';
import { AddUserComponent } from './component/add-user/add-user.component';
import { AddTaskComponent } from './component/add-task/add-task.component';
import { LoginComponent } from './component/login/login.component';


const appRoutes:Routes=[
  
  {path:'', component:HomeComponent},
  {path:'add_user', component:AddUserComponent},
  {path:'add_task', component:AddTaskComponent}
];
@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    AddUserComponent,
    AddTaskComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
