from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from students.models import Student

class StudentList(ListView):

    model = Student

class StudentCreate(CreateView):

    model = Student
    success_url = reverse_lazy("student_list")
    fields = ["name_student","email_student","password_student"]

class StudentUpdate(UpdateView):

    model = Student
    success_url = reverse_lazy("student_list")
    fields = ["name_student", "email_student", "password_student"]

class StudentDelete(DeleteView):

    model = Student
    success_url = reverse_lazy("student_list")