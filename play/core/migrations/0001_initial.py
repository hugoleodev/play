# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('sinopse', models.TextField(max_length=11)),
                ('capa', models.ImageField(upload_to=b'filmes/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
