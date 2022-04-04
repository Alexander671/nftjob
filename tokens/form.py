from django.forms import ModelForm, Textarea
from .models import Tokens
from django import forms

class TokensForm(ModelForm):
    class Meta:
        model = Tokens
        fields = ('media_url','owner')