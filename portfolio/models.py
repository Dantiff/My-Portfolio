
from __future__ import unicode_literals
import os
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
        return self.subject

class ProjectDomain(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    remove_date = models.DateTimeField(blank=True, null=True)

    def remove(self):
        self.remove_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
def get_image_path(instance, filename):
    return os.path.join('blogs', str(instance.id), filename)

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('Project', 'Project'),
        ('Blog', 'Blog'),
        ('Tutorial', 'Tutorial'),
    )
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Withdrawn', 'Withdrawn'),
    )
    title = models.CharField(max_length=200)
    author = models.OneToOneField(User)
    slug = models.SlugField(max_length=80, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='Blog',)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='Published',)
    domain = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    remove_date = models.DateTimeField(blank=True, null=True)

    def remove(self):
        self.remove_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Project Module'
        verbose_name_plural = 'Project Modules'

class Comment(models.Model):
    module = models.OneToOneField(Project)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_website = models.URLField(max_length=200)
    comment=models.TextField()

    def __unicode__(self):
        return '%s' % (self.comment)
