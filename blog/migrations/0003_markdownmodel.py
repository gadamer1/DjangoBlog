# Generated by Django 2.0.13 on 2019-05-23 05:07

from django.db import migrations, models
import django_markdownx.markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190516_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkdownModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfield', django_markdownx.markdownx.models.MarkdownxField()),
            ],
        ),
    ]
