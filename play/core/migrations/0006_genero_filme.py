# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='filme',
            field=models.ForeignKey(default=None, to='core.Filme'),
            preserve_default=False,
        ),
    ]
