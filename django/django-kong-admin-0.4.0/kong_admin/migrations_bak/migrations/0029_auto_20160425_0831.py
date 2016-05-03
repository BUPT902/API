# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0028_auto_20160425_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorreference',
            name='description',
            field=models.TextField(max_length=1024, verbose_name='\u9519\u8bef\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='headerreference',
            name='description',
            field=models.TextField(max_length=1024, null=True, verbose_name='\u53c2\u6570\u63cf\u8ff0', blank=True),
        ),
        migrations.AlterField(
            model_name='parameterreference',
            name='description',
            field=models.TextField(null=True, verbose_name='\u53c2\u6570\u63cf\u8ff0', blank=True),
        ),
        migrations.AlterField(
            model_name='servicereference',
            name='name',
            field=models.CharField(unique=True, max_length=1024, choices=[(b'1', '\u751f\u6d3b\u670d\u52a1'), (b'2', '\u5b9a\u4f4d\u670d\u52a1'), (b'3', '\u533b\u7597\u5065\u5eb7')]),
        ),
    ]
