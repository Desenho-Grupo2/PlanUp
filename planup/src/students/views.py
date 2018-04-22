from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterStudentForm,EditStudentForm

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