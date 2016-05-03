# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0011_auto_20160421_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apireference',
            name='request_host',
            field=models.CharField(default=None, max_length=32, null=True, help_text='The public DNS address that points to your API. For example, mockbin.com. At least request_host or request_path or both should be specified.', blank=True),
        ),
    ]
