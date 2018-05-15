from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import RegisterStudentForm,EditStudentForm
from subjects.models import Subject
from subjects.observer import SubjectConcreteObserver

observer = SubjectConcreteObserver()

@login_required
def show_student(request):

    print('\n\n')
    print(observer.dangerous_subjects)
    print('\n\n')

    context = {
        "subjects": Subject.objects.all(),
        "dangerous_subjects": observer.dangerous_subjects
    }

    return render(request, 'students/student_show.html',context)

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
            print('Form is NOT VALID.')
    else:

        form = RegisterStudentForm()

    return render(request, "students/student_new.html", {"form": form})

class StudentUpdate(UpdateView):

    model = EditStudentForm.Meta.model
    template_name = "students/student_edit.html"
    form_class = EditStudentForm

    def get_success_url(self):
        return reverse_lazy('show_student')

class StudentDelete(DeleteView):

    model = EditStudentForm.Meta.model
    template_name = "students/student_delete.html"

    def get_success_url(self):

        return reverse_lazy('logout')
