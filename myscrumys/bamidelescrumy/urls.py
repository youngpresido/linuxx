from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    
    # path('signup/',views.signup, name="signup"),
    path('login/',views.loginsystem,name="loginsystem"),
    path('test/',views.test,name="test"),
    path('add_user/',views.add_user,name="add_user"),
    path('add_task/',views.add_task,name="add_task"),
    path("goals/", views.GoalsView.as_view(), name="goals"),
    path('', views.index,name="index"),
   
    path('<id>/',views.singleuser,name="singleuser"),
    path('move_task/<int:task_id>/',views.move_task,name="move_task"),
    
    
    #path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    
    
]