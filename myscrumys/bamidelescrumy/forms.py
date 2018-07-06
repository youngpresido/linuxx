from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import ScrumyUser,ScrumyGoals,GoalStatus
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class AddUserForm(forms.ModelForm):
    # name=forms.CharField(max_length=200, help_text="the max length is 200")
    password=forms.CharField(label="Password", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    #role=forms.CharField(max_length=40)


    class Meta:
        model=ScrumyUser
        fields=['name','role','email','username']
    # def clean_email(self):
    #     email=self.cleaned_data.get('email')
    #     qs=ScrumyUser.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("email is taken")
    #     return email
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
        fields=['user','status','title','task']




class UserRegistration(UserCreationForm):
    email=forms.CharField(max_length=254, required=True,widget=forms.EmailInput())
    username=forms.CharField(max_length=100,required=True)
    class Meta:
        model=User
        fields=('username','email', 'password1','password2')
class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = ScrumyUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = ScrumyUser
        fields = ('username', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]