from django.db import models
from django.urls import reverse

from students.models import Student
from subjects.models import Subject

class Task(models.Model):

    task_name = models.CharField(max_length=200)
    task_text = models.CharField(max_length=1000,blank=True,null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_edit', kwargs={'pk': self.pk})

    def __str__(self):
        out  = 'Titulo tarefa: {}\n'.format(self.task_name)
        out  += 'Texto tarefa: {}\n'.format(self.task_text)
        return out

class TaskSubject(Task):

    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)

class TaskStudent(Task):

    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)