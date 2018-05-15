from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import ScrumyUser,ScrumyGoals,GoalStatus


class AddUserForm(forms.ModelForm):
    name=forms.CharField(max_length=200, help_text="the max length is 200")
    password=forms.CharField(label="Password", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    #role=forms.CharField(max_length=40)


    class Meta:
        model=ScrumyUser
        fields=['name','role','email','username']
    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=ScrumyUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

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
