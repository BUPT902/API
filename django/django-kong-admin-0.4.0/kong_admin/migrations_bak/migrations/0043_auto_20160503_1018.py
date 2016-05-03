# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0042_buyreference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyreference',
            name='api',
        ),
        migrations.RemoveField(
            model_name='buyreference',
            name='consumer',
        ),
        migrations.DeleteModel(
            name='BuyReference',
        ),
    ]
