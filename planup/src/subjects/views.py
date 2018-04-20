from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from subjects.models import Subject
from .forms import SubjectForm


def create_subject(request):

    subject = SubjectForm(request.POST or None)

    if subject.is_valid():
        subject.save()
        return redirect('list_subject')

    return render(request, 'subjects/new_subject.html', {'subject': subject})


def list_subject(request):

    subjects = Subject.objects.all()

    return render(request, 'subjects/list_subjects.html', {'subjects': subjects})
