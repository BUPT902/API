# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0003_auto_20160503_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api', models.ForeignKey(related_name='Buy_API', to='kong_admin.APIReference')),
                ('consumer', models.ForeignKey(related_name='Buy_consumer', verbose_name='\u7528\u6237', to='kong_admin.ConsumerReference')),
            ],
            options={
                'verbose_name': '\u8d2d\u4e70\u4fe1\u606f',
                'verbose_name_plural': '\u8d2d\u4e70\u4fe1\u606f',
            },
        ),
    ]
