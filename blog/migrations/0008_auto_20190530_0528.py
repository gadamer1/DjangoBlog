# Generated by Django 2.0.13 on 2019-05-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('POSTS', 'posts'), ('ALGORITHM', 'algorithm'), ('HACKING', 'hacking'), ('EATING', 'eating'), ('SERVICES', 'services')], default='POSTS', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='garbage', max_length=100, unique=True),
        ),
    ]
