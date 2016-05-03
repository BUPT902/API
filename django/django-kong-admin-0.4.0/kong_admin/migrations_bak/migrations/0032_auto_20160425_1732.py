# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0031_auto_20160425_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aclreference',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e'),
        ),
        migrations.AlterField(
            model_name='aclreference',
            name='synchronized_at',
            field=models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='aclreference',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e'),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e'),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='name',
            field=models.CharField(unique=True, default=None, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_.~-]+$', 'Enter a valid username. This value may contain only letters, numbers and ~/./-/_ characters.', 'invalid')], max_length=32, blank=True, help_text='The API name. If none is specified, will default to the request_host or request_path.', null=True, verbose_name='API\u82f1\u6587\u540d'),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='synchronized_at',
            field=models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e'),
        ),
        migrations.AlterField(
            model_name='basicauthreference',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e'),
        ),
        migrations.AlterField(
            model_name='basicauthreference',
            name='synchronized_at',
            field=models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='basicauthreference',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e'),
        ),
        migrations.AlterField(
            model_name='consumerreference',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e'),
        ),
        migrations.AlterField(
            model_name='consumerreference',
            name='synchronized_at',
            field=models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='consumerreference',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e'),
        ),
        migrations.AlterField(
            model_name='keyauthreference',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e'),
        ),
        migrations.AlterField(
            model_name='keyauthreference',
            name='synchronized_at',
            field=models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='keyauthreference',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e'),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e'),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='synchronized_at',
            field=models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e'),
        ),
        migrations.AlterField(
            model_name='pluginconfigurationreference',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e'),
        ),
        migrations.AlterField(
            model_name='pluginconfigurationreference',
            name='synchronized_at',
            field=models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='pluginconfigurationreference',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e'),
        ),
    ]
