from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import StudentForm

@login_required
def home(request):
    return render(request, 'students/student_show.html')

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.registration = form.cleaned_data.get("registration")
            user.username = form.cleaned_data.get("username")
            user.first_name = user.username
            user.username = user.profile.registration
            user.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'students/student_new.html', {'form': form})

