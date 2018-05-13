from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):

    class Meta:

        model = Subject
        fields = ("subject_name",
                  "subject_absence",
                  "number_credits",
                  "status",
                  "subject_code",)