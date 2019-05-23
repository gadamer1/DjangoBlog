# Generated by Django 2.0.13 on 2019-05-23 05:31

from django.db import migrations, models
import django.utils.timezone
import django_markdownx.markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_markdownmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mod_date', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=50)),
                ('body', django_markdownx.markdownx.models.MarkdownxField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='MarkdownModel',
        ),
    ]
