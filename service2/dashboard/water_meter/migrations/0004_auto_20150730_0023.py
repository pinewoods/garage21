# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_meter', '0003_auto_20150730_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensortype',
            name='unit',
            field=models.CharField(max_length=16),
        ),
    ]
