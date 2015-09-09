# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sabesp', '0002_auto_20150816_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('cnpj', models.CharField(max_length=18)),
                ('phone', models.CharField(max_length=16)),
                ('mobile', models.CharField(max_length=16, null=True)),
                ('cep', models.CharField(max_length=11, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
