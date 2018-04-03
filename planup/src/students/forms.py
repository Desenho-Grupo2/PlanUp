from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:

        model = Student
        fields = ("name_student","email_student","password_student","registration_student","age_of_birth_student")
