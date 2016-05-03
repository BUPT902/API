# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0035_auto_20160429_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aclreference',
            name='consumer',
            field=models.ForeignKey(related_name='aclreference_related', to='kong_admin.ConsumerReference'),
        ),
        migrations.AlterField(
            model_name='basicauthreference',
            name='consumer',
            field=models.ForeignKey(related_name='basicauthreference_related', to='kong_admin.ConsumerReference'),
        ),
        migrations.AlterField(
            model_name='keyauthreference',
            name='consumer',
            field=models.ForeignKey(related_name='keyauthreference_related', to='kong_admin.ConsumerReference'),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='consumer',
            field=models.ForeignKey(related_name='oauth2reference_related', to='kong_admin.ConsumerReference'),
        ),
    ]
