# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0013_auto_20160422_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apireference',
            name='owner',
            field=models.OneToOneField(related_name='infos', default=b'1', to='kong_admin.ConsumerReference', help_text='API\u6240\u5c5e\u4eba'),
        ),
    ]
