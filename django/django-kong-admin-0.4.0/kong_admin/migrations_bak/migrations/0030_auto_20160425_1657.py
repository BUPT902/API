# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0029_auto_20160425_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerreference',
            name='nessesary',
            field=models.BooleanField(default=True, verbose_name='\u5fc5\u586b'),
        ),
        migrations.AlterField(
            model_name='parameterreference',
            name='nessesary',
            field=models.BooleanField(verbose_name='\u5fc5\u586b'),
        ),
        migrations.AlterField(
            model_name='servicereference',
            name='name',
            field=models.CharField(unique=True, max_length=1024, verbose_name='\u670d\u52a1\u7c7b\u578b', choices=[(b'1', '\u751f\u6d3b\u670d\u52a1'), (b'2', '\u5b9a\u4f4d\u670d\u52a1'), (b'3', '\u533b\u7597\u5065\u5eb7')]),
        ),
    ]
