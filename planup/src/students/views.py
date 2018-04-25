from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegisterStudentForm,EditStudentForm
from .models import Student

@login_required
def show_student(request):



    return render(request, 'students/student_show.html')

def create_student(request):

    if request.method == 'POST':

        form = RegisterStudentForm(request.POST)

        if form.is_valid():

            user = form.save()
            user.refresh_from_db()
            user.profile.registration = form.cleaned_data.get("registration")
            user.username = form.cleaned_data.get("username")
            user.first_name = user.username
            user.username = user.profile.registration
            user.save()

            return redirect('/')
    else:

        form = RegisterStudentForm()

    return render(request, "students/student_new.html", {"form": form})

class StudentUpdate(UpdateView):

    model = EditStudentForm.Meta.model
    template_name = "students/student_edit.html"
    form_class = EditStudentForm

    def get_success_url(self):
        return reverse_lazy('show_student')

@login_required
def edit_student(request):

    if request.method == "POST":

        form = EditStudentForm(request.POST, instance=request.user)

        if form.is_valid():

            user = form.save()
            user.refresh_from_db()
            user.profile.registration = form.cleaned_data.get("registration")
            user.username = form.cleaned_data.get("username")
            user.first_name = user.username
            user.username = user.profile.registration
            user.save()

            return redirect(request, "students/student_show.html")

    else:

        form = EditStudentForm(request.POST, instance=request.user)

    return render(request, "students/student_edit.html", {"form": form})