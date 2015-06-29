# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('foto', django_resized.forms.ResizedImageField(upload_to=b'atores/')),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=100)),
                ('sinopse', models.TextField(max_length=11)),
                ('capa', django_resized.forms.ResizedImageField(upload_to=b'filmes/')),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'criado em')),
                ('atores', models.ManyToManyField(to='core.Ator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=20)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='filme',
            name='generos',
            field=models.ManyToManyField(to='core.Genero'),
            preserve_default=True,
        ),
    ]
