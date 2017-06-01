from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.TextField()
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    remove_date = models.DateTimeField(blank=True, null=True)

    def remove(self):
        self.remove_date = timezone.now()
        self.save()

    def __str__(self):
        return self.acc_name
