# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_person_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='joining_date',
            field=models.DateField(null=True),
        ),
    ]
