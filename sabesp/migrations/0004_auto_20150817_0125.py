# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sabesp', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cep',
            field=models.CharField(max_length=11, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=16, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=16, blank=True, null=True),
        ),
    ]
