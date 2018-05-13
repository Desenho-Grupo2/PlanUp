from django.shortcuts import render, redirect

from subjects.models import Subject
from students.models import Student
from .forms import SubjectForm


def create_subject(request):
    
    subject_form = SubjectForm(request.POST or None)

    if subject_form.is_valid():
        subject_form.save()

        return redirect("/dadosAluno")

    return render(request, "subjects/new_subject.html", {"subject_form": subject_form})


def list_subject(request):
    
    subjects = Subject.objects.all()

    return render(request, "subjects/list_subjects.html", {"subjects": subjects})


def update_subject(request, id):
    subject = Subject.objects.get(id=id)
    subject_form = SubjectForm(request.POST or None, instance=subject)

    if subject_form.is_valid():
        subject_form.save()
        return redirect("list_subject")

    return render(request, "subjects/update_subject.html", {"subject_form": subject_form, "subject": subject})


def delete_subject(request, id):

    subject = Subject.objects.get(id=id)

    if request.method == "POST":
        subject.delete()
        return redirect("list_subject")

    return render(request, "subjects/delete_confirm_subject.html", {"subject": subject})


def add_subject_student(request, pk):

    student = Student.objects.get(pk=request.user.id)
    subjects = Subject.objects.get(pk=pk)

    student.subject_set.add(subjects)
    student_list = student.subject_set.all()

    return render(request, "subjects/my_subjects_list.html", {"subjects": student_list})


def remove_subject_student(request, pk):

    student = Student.objects.get(pk=request.user.id)
    subject = Subject.objects.get(pk=pk)

    student.subject_set.remove(subject)
    student_list = student.subject_set.all()

    return render(request, "subjects/my_subjects_list.html", {"subjects":student_list})

def my_subjects(request):

    student = Student.objects.get(pk=request.user.id)
    student_list = student.subject_set.all()

    return render(request, "subjects/my_subjects_list.html", {"subjects": student_list})