# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sabesp', '0008_sabespprofile_sabesp_read_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabespreading',
            name='datestamp',
            field=models.DateField(default=datetime.datetime(2015, 8, 28, 14, 40, 40, 341323, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
