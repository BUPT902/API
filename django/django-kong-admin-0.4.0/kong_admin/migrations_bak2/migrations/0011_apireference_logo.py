# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0010_auto_20160504_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='apireference',
            name='logo',
            field=models.ImageField(default=b'defaut.jpg', null=True, upload_to=b'image', blank=True),
        ),
    ]
