# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0022_apireference_apicategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apireference',
            name='APIcategory',
            field=models.CharField(default=b'1', help_text='\u8bf7\u9009\u62e9API\u7684\u7c7b\u578b', max_length=10, verbose_name='API\u7c7b\u578b', choices=[(b'1', '\u5e73\u53f0API\u5e73\u53f0\u6570\u636e\u64cd\u4f5c'), (b'2', '\u5e73\u53f0API\u5e73\u53f0\u6570\u636e\u63d0\u4f9b'), (b'3', '\u5e73\u53f0\u529f\u80fdAPI'), (b'4', '\u5916\u90e8\u6ce8\u518cAPI')]),
        ),
        migrations.AlterField(
            model_name='keyauthreference',
            name='key_auth_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
