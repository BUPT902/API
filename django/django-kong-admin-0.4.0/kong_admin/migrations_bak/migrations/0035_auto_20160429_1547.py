# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0034_auto_20160429_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aclreference',
            name='consumer',
            field=models.ForeignKey(related_name='kong_admin_aclreference_related', to='kong_admin.ConsumerReference'),
        ),
        migrations.AlterField(
            model_name='basicauthreference',
            name='consumer',
            field=models.ForeignKey(related_name='kong_admin_basicauthreference_related', to='kong_admin.ConsumerReference'),
        ),
        migrations.AlterField(
            model_name='keyauthreference',
            name='consumer',
            field=models.ForeignKey(related_name='kong_admin_keyauthreference_related', to='kong_admin.ConsumerReference'),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='consumer',
            field=models.ForeignKey(related_name='kong_admin_oauth2reference_related', to='kong_admin.ConsumerReference'),
        ),
    ]
