
from __future__ import unicode_literals
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile_user')
    profile_name = models.CharField(max_length=200, null=True)
    subscribed = models.BooleanField(default=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    remove_date = models.DateTimeField(blank=True, null=True)

    def subscribe(self):
        self.subscribed = True
        self.save()

    def unsubscribe(self):
        self.subscribed = False
        self.save()

    def __str__(self):
        return self.user

class Message(models.Model):
    user = models.ForeignKey(User, related_name='message_user', on_delete=models.CASCADE, null=True)
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    remove_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.comment)

    def remove(self):
        self.show = False
        self.remove_date = timezone.now()
        self.save()
