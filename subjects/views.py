from django.shortcuts import render,redirect

from subjects.models import Subject
from .forms import SubjectForm

def create_subject(request):

    student = request.user
    subject_form = SubjectForm(request.POST or None)

    if subject_form.is_valid():

        subject_form.Meta.model.student = student.id
        subject_form.save()

        return redirect('/dadosAluno')

    return render(request, 'subjects/new_subject.html', {'subject_form': subject_form})


def list_subject(request):

    subjects = Subject.objects.all()

    return render(request, 'subjects/list_subjects.html', {'subjects': subjects})


def update_subject(request, id):
    subject = Subject.objects.get(id=id)
    subject_form = SubjectForm(request.POST or None, instance=subject)

    if subject_form.is_valid():
        subject_form.save()
        return redirect('list_subject')

    return render(request, 'subjects/update_subject.html', {'subject_form': subject_form, 'subject': subject})


def delete_subject(request, id):
    subject = Subject.objects.get(id=id)

    if request.method == 'POST':
        subject.delete()
        return redirect('list_subject')

    return render(request, 'subjects/delete_confirm_subject.html', {'subject': subject})
