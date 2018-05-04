from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import ScrumyUser,ScrumyGoals,GoalStatus


class AddUserForm(forms.ModelForm):
    name=forms.CharField(max_length=200, help_text="the max length is 200")
    email=forms.EmailField(max_length=70)
    #role=forms.CharField(max_length=40)


    class Meta:
        model=ScrumyUser
        fields=['name', 'email','role']

class AddTasks(forms.ModelForm):
    title=forms.CharField(max_length=200)
    task=forms.CharField(widget=forms.TextInput())


    class Meta:
        model=ScrumyGoals
        fields=['user_id','status','title','task']




class UserRegistration(UserCreationForm):
    email=forms.CharField(max_length=254, required=True,widget=forms.EmailInput())
    username=forms.CharField(max_length=100,required=True)
    class Meta:
        model=User
        fields=('username','email', 'password1','password2')
