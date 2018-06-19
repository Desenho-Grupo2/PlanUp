from django.shortcuts import render, redirect
import json

from subjects.models import Subject
from students.models import Student
from .forms import SubjectForm


def create_subject(request):
    
    subject_form = SubjectForm(request.POST or None)

    if subject_form.is_valid():

        subject = subject_form.save()
        student = Student.objects.get(pk=request.user.id)
        student.subject_set.add(subject)

        return redirect("minhas_disciplinas")

    return render(request, "subjects/new_subject.html", {"subject_form": subject_form})


def list_subject(request):
    
    subjects = Subject.objects.all()

    return render(request, "subjects/list_subjects.html", {"subjects": subjects})


def update_subject(request,id):

    subject = Subject.objects.get(id=id)
    subject_form = SubjectForm(request.POST or None, instance=subject)

    if subject_form.is_valid():

        subject_form.save()
        return redirect("minhas_disciplinas")

    return render(request, "subjects/update_subject.html", {"subject_form": subject_form, "subject": subject})


def delete_subject(request,id):

    subject = Subject.objects.get(id=id)

    if request.method == "POST":

        subject.delete()
        return redirect("list_subject")

    return render(request, "subjects/delete_confirm_subject.html", {"subject": subject})

def remove_subject_student(request,pk):

    subject = Subject.objects.get(pk=pk)
    subject.delete()

    return redirect('minhas_disciplinas')

def my_subjects(request):

    student = Student.objects.get(pk=request.user.id)
    student_list = student.subject_set.all()

    return render(request, "subjects/my_subjects_list.html", {"subjects": student_list})

from students.views import observer

def add_abscence(request, id):

    subject = Subject.objects.get(id=id)
    subject.attach(observer)

    subject.add_abscence()

    return redirect('minhas_disciplinas')

def subtract_abscence(request, id):

    subject = Subject.objects.get(id=id)
    subject.attach(observer)

    subject.subtract_abscence()

    return redirect('minhas_disciplinas')

def show_subjects_fga(request):

    subjects_fga = open('JSONS/DISCIPLINAS_FGA.json', 'r')
    read_subjects = json.load(subjects_fga)
    subjects_fga.close()

    list_cods = read_subjects
    tuples = []

    for aux in range(156):

        a = (list_cods['DISCIPLINAS_FGA']['CODIGO_DISCIPLINA'][aux])
        b = (list_cods['DISCIPLINAS_FGA']['MATERIA'][aux])

        tuples.append((a,b))


    return render(request, "subjects/subjects_fga.html", {"subjects":tuples})

def show_subjects_fce(request):

    subjects_fce = open('JSONS/DISCIPLINAS_FCE.json', 'r')
    read_subjects = json.load(subjects_fce)
    subjects_fce.close()

    list_cods = read_subjects
    tuples = []

    for aux in range(239):

        a = (list_cods['DISCIPLINAS_FCE']['CODIGO_DISCIPLINA'][aux])
        b = (list_cods['DISCIPLINAS_FCE']['MATERIA'][aux])

        tuples.append((a,b))


    return render(request, "subjects/subjects_fce.html", {"subjects":tuples})

def show_subjects_fup(request):

    subjects_fup = open('JSONS/DISCIPLINAS_FUP.json', 'r')
    read_subjects = json.load(subjects_fup)
    subjects_fup.close()

    list_cods = read_subjects
    tuples = []

    for aux in range(195):
        a = (list_cods['DISCIPLINAS_FUP']['CODIGO_DISCIPLINA'][aux])
        b = (list_cods['DISCIPLINAS_FUP']['MATERIA'][aux])

        tuples.append((a, b))

    return render(request, "subjects/subjects_fup.html", {"subjects": tuples})

def departaments_darcy(request):

    departaments_darcy = open('JSONS/DEPARTAMENTOS_DARCY.json', 'r')
    read_subjects = json.load(departaments_darcy)
    departaments_darcy.close()

    list_cods = read_subjects
    tuples = []

    for aux in range(76):
        a = (list_cods['DEPARTAMENTOS_DARCY']['CODIGO'][aux])
        b = (list_cods['DEPARTAMENTOS_DARCY']['SIGLA'][aux])
        c = (list_cods['DEPARTAMENTOS_DARCY']['DENOMINACAO'][aux])

        tuples.append((a, b,c))

    return render(request, "subjects/departaments_darcy.html", {"departaments": tuples})

def show_departaments(request):

    return render(request, "subjects/departaments.html")