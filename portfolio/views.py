import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.views import View
from portfolio.forms import *
from portfolio.models import *

class Index(View):
    template_name = 'index.html'
    form_class = MessageForm

    def get(self, request, *args, **kwargs):

        try:
            all_projects = Project.objects.all()
        except Project.DoesNotExist:
            return render(request, self.template_name,  {'projects': {}, 'tutorials': {}, 'blogs': {}, })

        projects = Project.objects.filter(category='Project')
        tutorials = Project.objects.filter(category='Tutorial')
        blogs = Project.objects.filter(category='Blog')

        return render(request, self.template_name,  {'projects': projects, 'tutorials': tutorials, 'blogs': blogs, })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message'],

            message = Message(
            name=name,
            email=email,
            subject=subject,
            message=message,
            )
            message.save()

            #send_mail(
            #    subject,
            #    message,
            #    email,
            #    ['danielmburu674@gmail.com'],
            #    fail_silently=False,
            #)
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})



class Blogs(View):
    template_name = 'blogs.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})




class Resume(View):

    def get(self, request, *args, **kwargs):
        """
        Send a file through Django without loading the whole file into
        memory at once. The FileWrapper will turn the file object into an
        iterator for chunks of 8KB.
        """
        filename = "/home/bivestinc/portfolio/media/Daniel_Resume_2017.pdf"
        wrapper = FileWrapper(open(filename, 'rb'))
        response = HttpResponse(wrapper, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
        response['Content-Length'] = os.path.getsize(filename)
        return response



