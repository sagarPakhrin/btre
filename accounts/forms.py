from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AccountsRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False, label='First Name' )
    last_name = forms.CharField(max_length=30,required=False, label='Last Name' )
    email = forms.EmailField(max_length=254, label='Email')
    username = forms.CharField(max_length=30, label='Username')
    class Meta():
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
