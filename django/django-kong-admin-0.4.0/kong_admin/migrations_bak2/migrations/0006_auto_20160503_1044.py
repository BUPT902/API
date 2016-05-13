# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0005_buyreference_created_at'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='buyreference',
            unique_together=set([('consumer', 'api')]),
        ),
    ]
