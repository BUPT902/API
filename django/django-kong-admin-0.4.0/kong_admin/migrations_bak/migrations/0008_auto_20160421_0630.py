# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0007_auto_20160414_0210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apireference',
            options={'verbose_name': 'API\u7ba1\u7406', 'verbose_name_plural': 'API\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='consumerreference',
            options={'verbose_name': '\u7528\u6237\u7ba1\u7406', 'verbose_name_plural': '\u7528\u6237\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='apireference',
            name='returnSample',
            field=models.CharField(max_length=1024, null=True, verbose_name='\u8fd4\u56de\u6837\u4f8b', blank=True),
        ),
    ]
