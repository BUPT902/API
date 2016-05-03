# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0020_auto_20160422_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apireference',
            name='owner',
            field=models.ForeignKey(related_name='infos', verbose_name='\u6240\u5c5e\u4eba', to_field=b'username', to='kong_admin.ConsumerReference', help_text='API\u6240\u5c5e\u4eba', null=True),
        ),
    ]
