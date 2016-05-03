# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0012_auto_20160421_0758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apireference',
            options={'verbose_name': 'API', 'verbose_name_plural': 'API'},
        ),
        migrations.AddField(
            model_name='apireference',
            name='owner',
            field=models.OneToOneField(related_name='infos', default=None, to='kong_admin.ConsumerReference', help_text='API\u6240\u5c5e\u4eba'),
        ),
    ]
