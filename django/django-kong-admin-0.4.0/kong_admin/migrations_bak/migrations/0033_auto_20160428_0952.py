# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0032_auto_20160425_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerreference',
            name='name',
            field=models.CharField(max_length=256, verbose_name='\u53c2\u6570\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='parameterreference',
            name='name',
            field=models.CharField(max_length=256, verbose_name='\u53c2\u6570\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='servicereference',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='\u670d\u52a1\u7c7b\u578b', choices=[(b'1', '\u751f\u6d3b\u670d\u52a1'), (b'2', '\u5b9a\u4f4d\u670d\u52a1'), (b'3', '\u533b\u7597\u5065\u5eb7')]),
        ),
        migrations.AlterUniqueTogether(
            name='headerreference',
            unique_together=set([('api', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='parameterreference',
            unique_together=set([('api', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='servicereference',
            unique_together=set([('api', 'name')]),
        ),
    ]
