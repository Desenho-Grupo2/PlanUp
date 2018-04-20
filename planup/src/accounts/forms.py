from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):

    username = forms.CharField(max_length=10,
                               widget=forms.TextInput(attrs={'name': 'registration'}))
    password = forms.CharField(max_length=14,
                               widget=forms.TextInput(attrs={'name': 'password'}))