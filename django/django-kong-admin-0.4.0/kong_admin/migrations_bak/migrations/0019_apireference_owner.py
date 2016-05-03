# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0018_remove_apireference_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='apireference',
            name='owner',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
