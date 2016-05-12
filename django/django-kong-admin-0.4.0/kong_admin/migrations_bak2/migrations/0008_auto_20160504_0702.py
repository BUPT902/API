# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0007_auto_20160504_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apireference',
            name='APIShort_description',
            field=models.TextField(help_text='\u8bf7\u8f93\u5165API\u7684\u7b80\u8981\u4ecb\u7ecd', null=True, verbose_name='API\u7b80\u8981\u7b80\u4ecb', blank=True),
        ),
    ]
