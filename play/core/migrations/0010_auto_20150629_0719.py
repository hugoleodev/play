# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_genero_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ator',
            name='foto',
            field=django_resized.forms.ResizedImageField(default=None, upload_to=b'atores/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ator',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
