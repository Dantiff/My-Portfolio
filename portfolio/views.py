import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views import View
from portfolio.forms import *
from portfolio.models import *
from django.contrib import messages


class Index(View):
    template_name = 'index.html'
    form_class = MessageForm

    def get(self, request, *args, **kwargs):

        try:
            posts_list = Project.objects.filter(status="Published").order_by('-created_date')
        except Project.DoesNotExist:

            messages.warning(request, 'Sorry, system our of reach.')

            return render(request, self.template_name,  {'recent_posts': {}, 'projects': {}, 'tutorials': {}, 'blogs': {}, })

        projects = Project.objects.filter(category='Project')
        tutorials = Project.objects.filter(category='Tutorial')
        blogs = Project.objects.filter(category='Blog')

        return render(request, self.template_name,  {'recent_posts': posts_list, 'projects': projects, 'tutorials': tutorials, 'blogs': blogs, })

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
            messages.success(request, 'Message sent successfully. I will get back to you as soon as I can. Thank you.')
            return HttpResponseRedirect('/')

        messages.error(request, 'Error posting message. Please check that you have filled all fields correctly.')

        return render(request, self.template_name, {'form': form})



class Blogs(View):
    blogs_template = 'blogs.html'

    def get(self, request, *args, **kwargs):

        try:
            posts_list = Project.objects.filter(status="Published").order_by('-created_date')
        except Project.DoesNotExist:

            messages.warning(request, 'Sorry, system out of reach.')

            return render(request, self.blogs_template,  {'posts': {}, 'recent_posts': {} })

        paginator = Paginator(posts_list, 5)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, self.blogs_template,  {'posts': posts, 'recent_posts': posts_list })



class Blog(View):
    blog_template = 'blog.html'

    def get(self, request, *args, **kwargs):


        try:
            posts_list = Project.objects.filter(status="Published").order_by('-created_date')
        except Project.DoesNotExist:

            messages.warning(request, 'Sorry, system out of reach.')

            return render(request, self.blog_template,  {'recent_posts': {}, 'post': {}})

        slug = self.kwargs['slug']

        try:
            post = Project.objects.get(slug=slug)
        except Project.DoesNotExist:

            messages.warning(request, 'Sorry, we could not retrieve the requested post.')

            return render(request, self.blog_template,  {'recent_posts': {}, 'post': {}})

        return render(request, self.blog_template,  {'recent_posts': posts_list, 'post': post })




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



