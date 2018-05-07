from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class RegisterStudentForm(UserCreationForm):

    registration = forms.CharField(max_length=14)

    class Meta:

        model = User
        fields = ('username', 'registration', 'password1', 'password2', 'email', 'first_name')


class EditStudentForm(UserChangeForm):

    first_name = forms.CharField(max_length=14, widget=forms.TextInput(
        attrs= {
            "class" :"form-control"
        }
    ), required=True)
    email = forms.EmailField(max_length=40, widget=forms.TextInput(
        attrs= {
            "class": "form-control"
        }
    ), required=True)

    username = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs= {
            "class": "form-control"
        }
    ),disabled=True)
    class Meta:

        model = User
        fields = ('username', 'password',"email", "first_name")