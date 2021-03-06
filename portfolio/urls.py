"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from portfolio.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view()),
    url(r'^users/unsubscribe/$', UnSubscribe.as_view()),
    url(r'^resume/download/$', Resume.as_view()),
    url(r'^blogs/$', Blogs.as_view()),
    url(r'^blogs/(?P<slug>\w+)/$', Blog.as_view()),
]




