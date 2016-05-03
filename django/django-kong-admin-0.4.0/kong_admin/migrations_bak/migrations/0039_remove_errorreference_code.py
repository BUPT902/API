# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0038_auto_20160503_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='errorreference',
            name='code',
        ),
    ]
