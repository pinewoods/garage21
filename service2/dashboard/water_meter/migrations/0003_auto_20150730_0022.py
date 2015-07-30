# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_meter', '0002_flow'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('code', models.CharField(unique=True, blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('unit', models.CharField(editable=False, max_length=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='flow',
            name='water_tank',
        ),
        migrations.AlterField(
            model_name='reading',
            name='sensor_reading',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Flow',
        ),
        migrations.AddField(
            model_name='reading',
            name='sensor_type',
            field=models.ForeignKey(default=1, to='water_meter.SensorType'),
            preserve_default=False,
        ),
    ]
