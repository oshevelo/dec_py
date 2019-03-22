# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-27 08:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationTry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_data', models.TextField(verbose_name='extra_data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_try', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
