from django.db import models
from django.urls import reverse

from students.models import Student
from . import observer

class Subject(models.Model, observer.ObserverSubject):

    student = models.ForeignKey(Student,null=True,blank=True,on_delete=models.CASCADE)
    subject_code = models.IntegerField(max_length=6)
    subject_name = models.CharField(max_length=40)
    subject_absence = models.IntegerField(max_length=3)
    number_credits = models.IntegerField(max_length=3)
    status = models.BooleanField(max_length=1)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subject_edit', kwargs={'pk': self.pk})

    def add_abscence(self):
        self.subject_absence += 1
        self.save()
        self.update()
        print('adding absence')

    def subtract_abscence(self):
        self.subject_absence -= 1
        self.save()
        self.update()

    def attach(self, observer):
        try:
            if self.observer is None:
                self.observer = observer
        except AttributeError:
            self.observer = observer

    def update(self):
        try:
            maximum_allowed_abscence = 2 * self.number_credits - 1
            if (self.subject_absence + 2) >= maximum_allowed_abscence:
                self.observer.update(self)
        except AttributeError:
            print('CANT UPDATE')
            pass

    def delete(self, using=None, keep_parents=False):
        try:
            self.observer.dangerous_subjects.discard(self)
            print('DELETING')
        except AttributeError:
            print('CANT DELETE')
            pass
        super().delete(using=using, keep_parents=keep_parents)
