# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0036_auto_20160429_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorreference',
            name='code',
            field=models.IntegerField(default=0, verbose_name='\u9519\u8bef\u7801'),
        ),
        migrations.AlterUniqueTogether(
            name='errorreference',
            unique_together=set([('api', 'code')]),
        ),
    ]
