# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0009_auto_20160421_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='apireference',
            name='remake',
            field=models.TextField(help_text='\u8bf7\u8f93\u5165\u5907\u6ce8', null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='API_description',
            field=models.TextField(help_text='\u8bf7\u8f93\u5165API\u63cf\u8ff0', null=True, verbose_name='API\u63cf\u8ff0', blank=True),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='returnSample',
            field=models.TextField(help_text='\u8bf7\u8f93\u51faAPI\u7684\u8fd4\u56de\u6837\u4f8b', null=True, verbose_name='\u8fd4\u56de\u6837\u4f8b', blank=True),
        ),
    ]
