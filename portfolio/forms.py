import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class MessageForm(forms.Form):

    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=300)


class SubscribeForm(forms.Form):

    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    website = forms.URLField(max_length=200, required=False)

