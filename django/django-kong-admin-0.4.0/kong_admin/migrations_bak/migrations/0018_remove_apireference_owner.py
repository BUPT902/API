# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0017_auto_20160422_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apireference',
            name='owner',
        ),
    ]
