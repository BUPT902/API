# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0008_auto_20160504_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='apireference',
            name='APIDayLimit',
            field=models.IntegerField(default=0, help_text='\u8bf7\u8f93\u5165API\u7684\u6bcf\u65e5\u8c03\u7528\u5cf0\u503c', verbose_name='\u6bcf\u79d2\u8c03\u7528\u5cf0\u503c'),
        ),
        migrations.AddField(
            model_name='apireference',
            name='APISecLimit',
            field=models.IntegerField(default=0, help_text='\u8bf7\u8f93\u5165API\u7684\u6bcf\u79d2\u8c03\u7528\u5cf0\u503c', verbose_name='\u6bcf\u79d2\u8c03\u7528\u5cf0\u503c'),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='API_description',
            field=models.TextField(help_text='\u8bf7\u8f93\u5165API\u4ecb\u7ecd', null=True, verbose_name='API\u4ecb\u7ecd', blank=True),
        ),
    ]
