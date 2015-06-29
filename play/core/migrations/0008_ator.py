# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150628_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('filme', models.ForeignKey(to='core.Filme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
