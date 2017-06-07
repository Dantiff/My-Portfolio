import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class MessageForm(forms.Form):

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows':6}))


class SubscribeForm(forms.Form):

    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    website = forms.URLField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Website'}))

