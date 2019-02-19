# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-02-19 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('easy', 'Very easy'), ('easy', 'Hard')], default='easy', max_length=200),
        ),
    ]
