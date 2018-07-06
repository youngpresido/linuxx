"""myscrumy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
import rest_framework
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from rest_framework.routers import DefaultRouter
from bamidelescrumy.apiviews import ScrumyUserList,ScrumyGoalsList,GoalStatusList
router=DefaultRouter()
router.register(r'scrumyusers',ScrumyUserList)
router.register(r'scrumygoals',ScrumyGoalsList)
router.register(r'goalstatus',GoalStatusList)
admin.autodiscover()
urlpatterns = [
    path('register/', include('rest_auth.registration.urls')),
    path('auth/', ObtainAuthToken.as_view()),
    # path('jwt-auth/',jwt_auth.views.obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('',include(router.urls)),
    path('bamidele/', include('bamidelescrumy.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    # path('api/',ScrumyUserList.as_view({'get':"list",'post':"create"})),
    # path('api/<int:pk>/',ScrumyUserList.as_view({'get':"list",'post':"create"})),
    # path('api/goals/',ScrumyGoalsList.as_view({'get':"list",'post':"create"})),
    # path('api/goals/<int:pk>/',ScrumyGoalsList.as_view({'get':"list",'post':"create"})),
    # path('api/status',GoalStatusList.as_view({'get':"list",'post':"create"})),
    # path('api/status/<int:pk>/',GoalStatusList.as_view({'get':"list",'post':"create"}))
    
]

