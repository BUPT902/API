# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0006_auto_20160503_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apireference',
            name='APIService_description',
        ),
        migrations.AddField(
            model_name='apireference',
            name='APIShort_description',
            field=models.TextField(help_text='\u8bf7\u8f93\u5165API\u7684\u7b80\u8981\u4ecb\u7ecd', null=True, verbose_name='API\u670d\u52a1\u7b80\u4ecb', blank=True),
        ),
    ]
