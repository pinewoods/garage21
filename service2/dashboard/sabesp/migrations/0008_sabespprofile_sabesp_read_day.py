# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sabesp', '0007_auto_20150821_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabespprofile',
            name='sabesp_read_day',
            field=models.FloatField(default=16),
            preserve_default=False,
        ),
    ]
