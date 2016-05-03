# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0025_auto_20160425_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyauthreference',
            name='key_auth_enabled',
        ),
    ]
