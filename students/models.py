from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration = models.CharField(max_length=14,null=True, blank=True,unique=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        student = Student(user=user)
        student.save()