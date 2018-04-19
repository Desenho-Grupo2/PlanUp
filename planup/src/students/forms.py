from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(UserCreationForm):

    registration = forms.CharField(max_length=14)

    class Meta:
        model = User
        fields = ('username', 'registration', 'password1', 'password2',"email","first_name")