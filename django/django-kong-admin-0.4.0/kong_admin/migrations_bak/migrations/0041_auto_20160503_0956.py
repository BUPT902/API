# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0040_auto_20160503_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumerreference',
            name='custom_id',
            field=models.CharField(help_text='Field for storing an existing ID for the consumer, useful for mapping Kong with users in your existing database. You must send either this field or username with the request.', max_length=48, null=True, blank=True),
        ),
    ]
