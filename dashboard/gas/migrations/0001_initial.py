# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pinewoods_timeseries', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CylinderWeight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('sensor_reading', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GasCylinder',
            fields=[
                ('channel_ptr', models.OneToOneField(parent_link=True, to='pinewoods_timeseries.Channel', serialize=False, primary_key=True, auto_created=True)),
                ('location', jsonfield.fields.JSONField()),
                ('cyclinder_type', models.CharField(choices=[('P45', 'P-45'), ('P90', 'P-90'), ('P190', 'P-190')], max_length=4)),
            ],
            bases=('pinewoods_timeseries.channel',),
        ),
        migrations.AddField(
            model_name='cylinderweight',
            name='channel',
            field=models.ForeignKey(to='gas.GasCylinder'),
        ),
    ]
