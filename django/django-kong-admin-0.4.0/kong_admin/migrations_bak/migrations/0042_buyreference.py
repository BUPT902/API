# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0041_auto_20160503_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api', models.ForeignKey(related_name='Buy_API', to='kong_admin.APIReference')),
                ('consumer', models.ForeignKey(related_name='Buy_consumer', to='kong_admin.ConsumerReference')),
            ],
        ),
    ]
