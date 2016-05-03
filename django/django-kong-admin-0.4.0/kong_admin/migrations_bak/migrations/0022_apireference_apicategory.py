# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0021_auto_20160422_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='apireference',
            name='APIcategory',
            field=models.CharField(default=b'1', max_length=10, choices=[(b'1', '\u5e73\u53f0API\u5e73\u53f0\u6570\u636e\u64cd\u4f5c'), (b'2', '\u5e73\u53f0API\u5e73\u53f0\u6570\u636e\u63d0\u4f9b'), (b'3', '\u5e73\u53f0\u529f\u80fdAPI'), (b'4', '\u5916\u90e8\u6ce8\u518cAPI')]),
        ),
    ]
