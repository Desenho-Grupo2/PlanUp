from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterStudentForm(UserCreationForm):

    registration = forms.CharField(max_length=14)

    class Meta:

        model = User
        fields = ('username', 'registration', 'password1', 'password2',"email","first_name")


class EditStudentForm(forms.ModelForm):

    registration = forms.CharField(max_length=14)
    username = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    first_name = forms.CharField(max_length=40)

    class Meta:

        model = User
        fields = ('username', 'registration',"email", "first_name")

    def save(self, commit=True):

        user = super(EditStudentForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.refresh_from_db()
        user.profile.registration = self.cleaned_data.get("registration")
        user.username = self.cleaned_data.get("username")
        user.first_name = user.username
        user.username = user.profile.registration

        if commit:
            user.save()

        return user
