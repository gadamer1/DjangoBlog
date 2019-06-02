from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_markdownx.markdownx.models import MarkdownxField
from django.utils.text import slugify
from django.utils.http import urlencode
from django_markdownx.markdownx.utils import markdownify
from unidecode import unidecode
class Post(models.Model):
    CATEGORY_CHOICES=(
        ('POSTS','posts'),
        ('ALGORITHM','algorithm'),
        ('HACKING','hacking'),
        ('EATING','eating'),
        ('SERVICES','services'),
    )

    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    snippet = models.CharField(max_length=200, default='hello!')
    body = MarkdownxField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    slug = models.SlugField(max_length=100,default='garbage',allow_unicode =True)
    thumb_nail = models.ImageField(default = 'default.png')
    category=models.CharField(max_length=100, choices = CATEGORY_CHOICES,default='POSTS')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    def my_slugify(self):
        self.slug = slugify(unidecode(self.title))
        
    def formatted_markdownx(self):
        return markdownify(self.body)
