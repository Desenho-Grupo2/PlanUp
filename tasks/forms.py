from django import forms
from .models import TaskStudent,TaskSubject

class TaskFormSubject(forms.ModelForm):

    class Meta:

        model = TaskSubject
        fields = ("task_name","task_text")

class TaskFormStudent(forms.ModelForm):

    class Meta:

        model = TaskStudent
        fields = ("task_name","task_text")