# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sabesp', '0009_sabespreading_datestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(max_length=64, unique=True)),
                ('rate', models.FloatField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('consumer_type', models.ForeignKey(to='sabesp.ConsumerType')),
            ],
            options={
                'verbose_name_plural': 'taxes',
            },
        ),
        migrations.RenameModel(
            old_name='HidrometroSabesp',
            new_name='SabespWatermeter',
        ),
        migrations.RemoveField(
            model_name='taxe',
            name='consumer_type',
        ),
        migrations.RenameField(
            model_name='sabespreading',
            old_name='sensor_id',
            new_name='watermeter',
        ),
        migrations.AlterField(
            model_name='sabespreading',
            name='reading_m3',
            field=models.FloatField(),
        ),
        migrations.AlterUniqueTogether(
            name='sabespreading',
            unique_together=set([('reading_competence', 'watermeter')]),
        ),
        migrations.DeleteModel(
            name='Taxe',
        ),
        migrations.RemoveField(
            model_name='sabespreading',
            name='sabesp_profile',
        ),
    ]
