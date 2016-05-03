# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0026_remove_keyauthreference_key_auth_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=256, verbose_name='\u9519\u8bef\u4fe1\u606f')),
                ('description', models.CharField(max_length=1024, verbose_name='\u9519\u8bef\u63cf\u8ff0')),
                ('api', models.ForeignKey(related_name='Error', to='kong_admin.APIReference', help_text='\u8bf7\u6dfb\u52a0API\u7684\u9519\u8bef\u8868')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256, verbose_name='\u53c2\u6570\u540d\u79f0')),
                ('type', models.CharField(max_length=256, verbose_name='\u53c2\u6570\u7c7b\u578b')),
                ('description', models.CharField(max_length=1024, verbose_name='\u53c2\u6570\u63cf\u8ff0')),
                ('defaultValue', models.CharField(max_length=256, verbose_name='\u9ed8\u8ba4\u503c')),
                ('nessesary', models.BooleanField(default=True, verbose_name='\u662f\u5426\u5fc5\u586b')),
                ('api', models.ForeignKey(related_name='Header', to='kong_admin.APIReference', help_text='\u8bf7\u6dfb\u52a0API\u7684header\u53c2\u6570')),
            ],
        ),
        migrations.CreateModel(
            name='ParameterReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256, verbose_name='\u53c2\u6570\u540d\u79f0')),
                ('type', models.CharField(max_length=256, verbose_name='\u53c2\u6570\u7c7b\u578b')),
                ('description', models.CharField(max_length=1024, verbose_name='\u53c2\u6570\u63cf\u8ff0')),
                ('defaultValue', models.CharField(max_length=256, verbose_name='\u9ed8\u8ba4\u503c')),
                ('nessesary', models.BooleanField(verbose_name='\u662f\u5426\u5fc5\u586b')),
                ('api', models.ForeignKey(related_name='Parameter', to='kong_admin.APIReference', help_text='\u8bf7\u6dfb\u52a0API\u7684url\u53c2\u6570')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=256, verbose_name='\u9519\u8bef\u4fe1\u606f')),
                ('description', models.CharField(max_length=1024, verbose_name='\u9519\u8bef\u63cf\u8ff0')),
                ('name', models.CharField(max_length=1024, choices=[(b'1', '\u751f\u6d3b\u670d\u52a1'), (b'2', '\u5b9a\u4f4d\u670d\u52a1'), (b'3', '\u533b\u7597\u5065\u5eb7')])),
                ('api', models.ForeignKey(related_name='Service', to='kong_admin.APIReference', help_text='\u8bf7\u6dfb\u52a0API\u7684\u670d\u52a1\u7c7b\u578b\u8868')),
            ],
        ),
    ]
