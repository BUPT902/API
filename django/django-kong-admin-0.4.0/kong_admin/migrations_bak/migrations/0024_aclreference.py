# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0023_auto_20160422_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='AclReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='synchronized', null=True, editable=False, blank=True)),
                ('group', models.CharField(help_text='\u8bf7\u8f93\u5165\u7528\u6237\u6240\u5c5e\u7684\u7ec4', unique=True, max_length=32)),
                ('consumer', models.ForeignKey(to='kong_admin.ConsumerReference')),
            ],
            options={
                'verbose_name': 'Acl Reference',
                'verbose_name_plural': 'Acl References',
            },
        ),
    ]
