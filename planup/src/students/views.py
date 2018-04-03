from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from students.models import Student
from .forms import StudentForm

class StudentList(ListView):
    model = Student

class StudentCreate(CreateView):

    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("student_list")
    template_name = "students/student_new.html"

class StudentUpdate(UpdateView):
    model = Student
    success_url = reverse_lazy("student_list")
    fields = ["name_student", "email_student", "password_student", "registration_student","age_of_birth"]
    template_name_suffix = "_update_form"


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy("student_list")


class StudentShow(DetailView):
    model = Student
    success_url = reverse_lazy("student_list")

