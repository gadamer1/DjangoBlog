from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','snippet','slug','thumb_nail',]
