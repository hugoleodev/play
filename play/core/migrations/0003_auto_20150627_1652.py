# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_filme_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filme',
            name='capa',
            field=django_resized.forms.ResizedImageField(upload_to=b'filmes/'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'criado em'),
        ),
    ]
