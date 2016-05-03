# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0010_auto_20160421_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='apireference',
            name='APIChineseName',
            field=models.CharField(default=None, max_length=32, blank=True, help_text='\u8bf7\u8f93\u5165API\u7684\u4e2d\u6587\u540d', null=True, verbose_name='API\u4e2d\u6587\u540d'),
        ),
        migrations.AddField(
            model_name='apireference',
            name='requestType',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
