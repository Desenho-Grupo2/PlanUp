from django.shortcuts import render, redirect

from subjects.models import Subject,Student
from .forms import TaskFormSubject,TaskFormStudent
from tasks.models import Task, TaskStudent, TaskSubject

def create_task_subject(request,subject_pk):

    subject_task_form = TaskFormSubject(request.POST or None)
    subject = Subject.objects.get(pk=subject_pk)

    if subject_task_form.is_valid():

        subject_task = subject_task_form.save(commit=False)

        subject_task.subject = subject
        subject_task.save()

        return redirect("task_list")

    return render(request, "new_task.html", {"subject_task_form": subject_task_form})

def create_task_student(request):

    student_task_form = TaskFormStudent(request.POST or None)
    student = Student.objects.get(pk=request.user.id)

    if student_task_form.is_valid():

        student_task = student_task_form.save(commit=False)

        student_task.student = student
        print('\n\nsalvando:')
        student_task.save()
        print('student_task = {}'.format(student_task))

        return redirect("task_list")

    return render(request, "new_task.html", {"subject_task_form": student_task_form})

def task_list(request):

#    tasks = Task.objects.all()

    subject_tasks = TaskSubject.objects.all()
    student_tasks = TaskStudent.objects.all()

    context = {"subject_tasks": subject_tasks,
               "student_tasks": student_tasks}

    return render(request, "my_tasks_list.html", context)

def update_task(request,id):

    task = Task.objects.get(id=id)
    task_form = TaskFormSubject(request.POST or None, instance=task)

    if task_form.is_valid():

        task_form.save()
        return redirect("task_list")

    return render(request, "update_task.html", {"task": task})

def delete_task(request,id):

    task = Task.objects.get(id=id)

    if request.method == "POST":

        task.delete()
        return redirect("task_list")

    return render(request, "delete_task.html", {"task": task})