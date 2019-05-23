from django import forms
from . import models
from django_markdownx.markdownx.fields import MarkdownxFormField

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','text','slug','thumb_nail']


class Markdownx(forms.ModelForm):
    myfield= MarkdownxFormField()