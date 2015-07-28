# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_meter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sensor_reading', models.IntegerField(editable=False)),
                ('water_tank', models.ForeignKey(to='water_meter.WaterTank')),
            ],
        ),
    ]
