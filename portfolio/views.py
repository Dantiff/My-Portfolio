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
        return render(request, self.template_name)

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
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})




