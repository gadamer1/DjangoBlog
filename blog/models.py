from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_markdownx.markdownx.models import MarkdownxField

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    slug = models.SlugField(max_length=100,default='garbage')
    thumb_nail = models.ImageField(default = 'default.png')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def snippet(self):
        if len(self.text)>=100:
            return self.text[:100]+'...'
        else:
            return self.text[:100]


#markdownx

class DateCreateModMixin(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateTimeField(default=timezone.now)
    mod_date = models.DateTimeField(blank=True, null=True)

class BlogPost(DateCreateModMixin):
    title = models.CharField(max_length=50)
    body = MarkdownxField()