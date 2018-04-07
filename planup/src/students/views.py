from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect

from students.models import Student
from .forms import StudentForm

def create_student(request):

    if request.method == 'POST':

        student = StudentForm(request.POST)

        if student.is_valid():
            student.save()
            return HttpResponseRedirect('/')

    else:
        student = StudentForm()

    return render(request, 'students/student_new.html', {'student': student})

def edit_student(request,pk):

    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':

        form = StudentForm(request.POST,instance=student)

        if form.is_valid():

            student = form.save(commit=False)

            student.save()
            return redirect('student_show',pk=student.pk)

    else:

        form = StudentForm(instance=student)

    return render(request, 'students/student_edit.html', {'student':student})

def delete_student(request,pk):

    student = get_object_or_404(Student,pk=pk)

    if request.method == 'POST':

        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_delete.html', {'student':student})

class StudentList(ListView):

    model = Student

def show_student(request,pk):

    student = get_object_or_404(Student,pk=pk)

    form = StudentForm(request.POST, instance=student)

    if form.is_valid():
        student = form.save(commit=False)

        student.save()
        return redirect('student_show', pk=student.pk)

    return render(request, 'students/student_show.html', {'student': student})

def student_list(request):

    student = Student.objects.all()

    return render(request, 'students/student_list.html', {'object_list':student})