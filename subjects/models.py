from django.db import models
from django.urls import reverse

from students.models import Student

class Subject(models.Model):

    student = models.ForeignKey(Student,null=True,blank=True,on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=40)
    subject_absence = models.IntegerField(max_length=3)
    number_credits = models.IntegerField(max_length=3)
    status = models.BooleanField(max_length=1)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subject_edit', kwargs={'pk': self.pk})