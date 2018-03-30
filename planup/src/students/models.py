from django.db import models
from django.core.urlresolvers import reverse

class Student(models.Model):

    name_student = models.CharField(max_length=40)
    email_student = models.EmailField(max_length=40)
    password_student = models.CharField(max_length=14)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student_edit', kwargs={'pk': self.pk})