# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0008_auto_20160421_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apireference',
            name='returnSample',
            field=models.TextField(null=True, verbose_name='\u8fd4\u56de\u6837\u4f8b', blank=True),
        ),
    ]
