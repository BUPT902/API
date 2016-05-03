# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0002_auto_20160503_1025'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='errorreference',
            unique_together=set([('api', 'code')]),
        ),
    ]
