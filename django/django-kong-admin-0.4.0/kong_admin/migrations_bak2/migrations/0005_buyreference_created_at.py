# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0004_buyreference'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyreference',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 3, 2, 41, 52, 458584, tzinfo=utc), verbose_name='\u521b\u5efa\u4e8e', auto_now_add=True),
            preserve_default=False,
        ),
    ]
