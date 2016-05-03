# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0027_errorreference_headerreference_parameterreference_servicereference'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='errorreference',
            options={'verbose_name': '\u9519\u8bef\u53c2\u6570', 'verbose_name_plural': '\u9519\u8bef\u53c2\u6570\u8868'},
        ),
        migrations.AlterModelOptions(
            name='headerreference',
            options={'verbose_name': 'header\u53c2\u6570', 'verbose_name_plural': 'header\u53c2\u6570\u8868'},
        ),
        migrations.AlterModelOptions(
            name='parameterreference',
            options={'verbose_name': 'url\u53c2\u6570', 'verbose_name_plural': 'url\u53c2\u6570\u8868'},
        ),
        migrations.AlterModelOptions(
            name='servicereference',
            options={'verbose_name': '\u670d\u52a1\u7c7b\u578b', 'verbose_name_plural': '\u670d\u52a1\u7c7b\u578b'},
        ),
        migrations.RemoveField(
            model_name='servicereference',
            name='description',
        ),
        migrations.RemoveField(
            model_name='servicereference',
            name='message',
        ),
    ]
