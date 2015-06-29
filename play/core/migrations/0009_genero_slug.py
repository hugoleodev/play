# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_ator'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
