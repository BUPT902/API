# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0033_auto_20160428_0952'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servicereference',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='servicereference',
            name='api',
        ),
        migrations.AddField(
            model_name='apireference',
            name='APIService_category',
            field=models.CharField(default=b'1', help_text='\u8bf7\u9009\u62e9API\u7684\u670d\u52a1\u7c7b\u578b', max_length=10, verbose_name='\u670d\u52a1\u7c7b\u578b', choices=[(b'1', '\u6570\u636e\u64cd\u4f5c'), (b'2', '\u751f\u6d3b\u670d\u52a1'), (b'3', '\u5b9a\u4f4d\u670d\u52a1'), (b'4', '\u4ea4\u901a\u4fe1\u606f')]),
        ),
        migrations.AddField(
            model_name='apireference',
            name='APIService_description',
            field=models.TextField(help_text='\u8bf7\u8f93\u51faAPI\u7684\u670d\u52a1\u4ecb\u7ecd', null=True, verbose_name='API\u670d\u52a1\u7b80\u4ecb', blank=True),
        ),
        migrations.AddField(
            model_name='apireference',
            name='dataFileName',
            field=models.CharField(help_text='API\u64cd\u4f5c\u6570\u636e\u6587\u4ef6\u7684\u540d\u79f0', max_length=256, null=True, verbose_name='API\u64cd\u4f5c\u6570\u636e\u6587\u4ef6\u7684\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='requestType',
            field=models.CharField(default=b'1', help_text='\u8bf7\u9009\u62e9API\u7684\u8bf7\u6c42\u7c7b\u578b', max_length=10, verbose_name='API\u8bf7\u6c42\u7c7b\u578b', choices=[(b'1', b'GET'), (b'2', b'POST'), (b'3', b'PATCH'), (b'4', b'DELETE')]),
        ),
        migrations.DeleteModel(
            name='ServiceReference',
        ),
    ]
