# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0024_aclreference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aclreference',
            name='group',
            field=models.CharField(help_text='\u8bf7\u8f93\u5165\u7528\u6237\u6240\u5c5e\u7684\u7ec4', unique=True, max_length=32, verbose_name='\u7528\u6237\u7ec4'),
        ),
    ]
