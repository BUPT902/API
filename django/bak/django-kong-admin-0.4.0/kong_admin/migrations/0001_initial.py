# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AclReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True)),
                ('group', models.CharField(help_text='\u8bf7\u8f93\u5165\u7528\u6237\u6240\u5c5e\u7684\u7ec4', unique=True, max_length=32, verbose_name='\u7528\u6237\u7ec4')),
            ],
            options={
                'verbose_name': 'Acl Reference',
                'verbose_name_plural': 'Acl References',
            },
        ),
        migrations.CreateModel(
            name='APIReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True)),
                ('upstream_url', models.URLField(help_text='The base target URL that points to your API server, this URL will be used for proxying requests. For example, https://mockbin.com.')),
                ('name', models.CharField(unique=True, default=None, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_.~-]+$', 'Enter a valid username. This value may contain only letters, numbers and ~/./-/_ characters.', 'invalid')], max_length=32, blank=True, help_text='The API name. If none is specified, will default to the request_host or request_path.', null=True, verbose_name='API\u82f1\u6587\u540d')),
                ('dataFileName', models.CharField(help_text='API\u64cd\u4f5c\u6570\u636e\u6587\u4ef6\u7684\u540d\u79f0', max_length=256, null=True, verbose_name='API\u64cd\u4f5c\u6570\u636e\u6587\u4ef6\u7684\u540d\u79f0', blank=True)),
                ('APIChineseName', models.CharField(default=None, max_length=32, blank=True, help_text='\u8bf7\u8f93\u5165API\u7684\u4e2d\u6587\u540d', null=True, verbose_name='API\u4e2d\u6587\u540d')),
                ('request_host', models.CharField(default=None, max_length=32, null=True, help_text='The public DNS address that points to your API. For example, mockbin.com. At least request_host or request_path or both should be specified.', blank=True)),
                ('request_path', models.CharField(default=None, max_length=32, null=True, help_text='The public path that points to your API. For example, /someservice. At least request_host or request_path or both should be specified.', blank=True)),
                ('preserve_host', models.BooleanField(default=False, help_text='Preserves the original Host header sent by the client, instead of replacing it with the hostname of the upstream_url. By default is false.')),
                ('strip_request_path', models.BooleanField(default=False, help_text='Strip the request_path value before proxying the request to the final API. For example a request made to /someservice/hello will be resolved to upstream_url/hello. By default is false.')),
                ('enabled', models.BooleanField(default=True)),
                ('API_description', models.TextField(help_text='\u8bf7\u8f93\u5165API\u63cf\u8ff0', null=True, verbose_name='API\u63cf\u8ff0', blank=True)),
                ('returnSample', models.TextField(help_text='\u8bf7\u8f93\u51faAPI\u7684\u8fd4\u56de\u6837\u4f8b', null=True, verbose_name='\u8fd4\u56de\u6837\u4f8b', blank=True)),
                ('remake', models.TextField(help_text='\u8bf7\u8f93\u5165\u5907\u6ce8', null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('APIcategory', models.CharField(default=b'1', help_text='\u8bf7\u9009\u62e9API\u7684\u7c7b\u578b', max_length=10, verbose_name='API\u7c7b\u578b', choices=[(b'1', '\u5e73\u53f0API\u5e73\u53f0\u6570\u636e\u64cd\u4f5c'), (b'2', '\u5e73\u53f0API\u5e73\u53f0\u6570\u636e\u63d0\u4f9b'), (b'3', '\u5e73\u53f0\u529f\u80fdAPI'), (b'4', '\u5916\u90e8\u6ce8\u518cAPI')])),
                ('requestType', models.CharField(default=b'1', help_text='\u8bf7\u9009\u62e9API\u7684\u8bf7\u6c42\u7c7b\u578b', max_length=10, verbose_name='API\u8bf7\u6c42\u7c7b\u578b', choices=[(b'1', b'GET'), (b'2', b'POST'), (b'3', b'PATCH'), (b'4', b'DELETE')])),
                ('APIService_category', models.CharField(default=b'1', help_text='\u8bf7\u9009\u62e9API\u7684\u670d\u52a1\u7c7b\u578b', max_length=10, verbose_name='\u670d\u52a1\u7c7b\u578b', choices=[(b'1', '\u6570\u636e\u64cd\u4f5c'), (b'2', '\u751f\u6d3b\u670d\u52a1'), (b'3', '\u5b9a\u4f4d\u670d\u52a1'), (b'4', '\u4ea4\u901a\u4fe1\u606f')])),
                ('APIService_description', models.TextField(help_text='\u8bf7\u8f93\u51faAPI\u7684\u670d\u52a1\u4ecb\u7ecd', null=True, verbose_name='API\u670d\u52a1\u7b80\u4ecb', blank=True)),
            ],
            options={
                'verbose_name': 'API',
                'verbose_name_plural': 'API',
            },
        ),
        migrations.CreateModel(
            name='BasicAuthReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True)),
                ('username', models.CharField(help_text='The username to use in the Basic Authentication', unique=True, max_length=32)),
                ('password', models.CharField(help_text='The password to use in the Basic Authentication', max_length=40)),
            ],
            options={
                'verbose_name': 'Basic Auth Reference',
                'verbose_name_plural': 'Basic Auth References',
            },
        ),
        migrations.CreateModel(
            name='ConsumerReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True)),
                ('username', models.CharField(help_text='The username of the consumer. You must send either this field or custom_id with the request.', max_length=32, unique=True, null=True, blank=True)),
                ('custom_id', models.CharField(help_text='Field for storing an existing ID for the consumer, useful for mapping Kong with users in your existing database. You must send either this field or username with the request.', max_length=48, null=True, blank=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='ErrorReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(default=0, verbose_name='\u9519\u8bef\u7801')),
                ('message', models.CharField(max_length=256, verbose_name='\u9519\u8bef\u4fe1\u606f')),
                ('description', models.TextField(max_length=1024, verbose_name='\u9519\u8bef\u63cf\u8ff0')),
                ('api', models.ForeignKey(related_name='Error', to='kong_admin.APIReference', help_text='\u8bf7\u6dfb\u52a0API\u7684\u9519\u8bef\u8868')),
            ],
            options={
                'verbose_name': '\u9519\u8bef\u53c2\u6570',
                'verbose_name_plural': '\u9519\u8bef\u53c2\u6570\u8868',
            },
        ),
        migrations.CreateModel(
            name='HeaderReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u53c2\u6570\u540d\u79f0')),
                ('type', models.CharField(max_length=256, verbose_name='\u53c2\u6570\u7c7b\u578b')),
                ('description', models.TextField(max_length=1024, null=True, verbose_name='\u53c2\u6570\u63cf\u8ff0', blank=True)),
                ('defaultValue', models.CharField(max_length=256, verbose_name='\u9ed8\u8ba4\u503c')),
                ('nessesary', models.BooleanField(default=True, verbose_name='\u5fc5\u586b')),
                ('api', models.ForeignKey(related_name='Header', to='kong_admin.APIReference', help_text='\u8bf7\u6dfb\u52a0API\u7684header\u53c2\u6570')),
            ],
            options={
                'verbose_name': 'header\u53c2\u6570',
                'verbose_name_plural': 'header\u53c2\u6570\u8868',
            },
        ),
        migrations.CreateModel(
            name='KeyAuthReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True)),
                ('key', models.UUIDField(help_text='You can optionally set your own unique key to authenticate the client. If missing, the plugin will generate one.', null=True, editable=False, blank=True)),
                ('consumer', models.ForeignKey(related_name='keyauthreference_related', to='kong_admin.ConsumerReference')),
            ],
            options={
                'verbose_name': 'Key Auth Reference',
                'verbose_name_plural': 'Key Auth References',
            },
        ),
        migrations.CreateModel(
            name='OAuth2Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True)),
                ('name', models.CharField(help_text='The name to associate to the credential. In OAuth 2.0 this would be the application name.', unique=True, max_length=32)),
                ('redirect_uri', models.URLField(help_text='The URL in your app where users will be sent after authorization (RFC 6742 Section 3.1.2)')),
                ('client_id', models.CharField(help_text='You can optionally set your own unique client_id. If missing, the plugin will generate one.', max_length=64, unique=True, null=True, blank=True)),
                ('client_secret', models.TextField(help_text='You can optionally set your own unique client_secret. If missing, the plugin will generate one.', null=True, blank=True)),
                ('consumer', models.ForeignKey(related_name='oauth2reference_related', to='kong_admin.ConsumerReference')),
            ],
            options={
                'verbose_name': 'OAuth2 Reference',
                'verbose_name_plural': 'OAuth2 References',
            },
        ),
        migrations.CreateModel(
            name='ParameterReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u53c2\u6570\u540d\u79f0')),
                ('type', models.CharField(max_length=256, verbose_name='\u53c2\u6570\u7c7b\u578b')),
                ('description', models.TextField(null=True, verbose_name='\u53c2\u6570\u63cf\u8ff0', blank=True)),
                ('defaultValue', models.CharField(max_length=256, verbose_name='\u9ed8\u8ba4\u503c')),
                ('nessesary', models.BooleanField(verbose_name='\u5fc5\u586b')),
                ('api', models.ForeignKey(related_name='Parameter', to='kong_admin.APIReference', help_text='\u8bf7\u6dfb\u52a0API\u7684url\u53c2\u6570')),
            ],
            options={
                'verbose_name': 'url\u53c2\u6570',
                'verbose_name_plural': 'url\u53c2\u6570\u8868',
            },
        ),
        migrations.CreateModel(
            name='PluginConfigurationReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u4e8e')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='\u540c\u6b65\u4e8e', null=True, editable=False, blank=True)),
                ('plugin', models.IntegerField(default=13, help_text="The name of the Plugin that's going to be added. Currently the Plugin must be installed in every Kong instance separately.")),
                ('enabled', models.BooleanField(default=True)),
                ('config', jsonfield2.fields.JSONField(default={}, help_text='The configuration properties for the Plugin which can be found on the plugins documentation page in the Plugin Gallery.')),
                ('api', models.ForeignKey(related_name='plugins', to='kong_admin.APIReference', help_text='The API on which to add a plugin configuration')),
                ('consumer', models.ForeignKey(related_name='plugins', blank=True, to='kong_admin.ConsumerReference', help_text='The consumer that overrides the existing settings for this specific consumer on incoming requests.', null=True)),
            ],
            options={
                'verbose_name': 'Plugin Configuration Reference',
                'verbose_name_plural': 'Plugin Configuration References',
            },
        ),
        migrations.AddField(
            model_name='basicauthreference',
            name='consumer',
            field=models.ForeignKey(related_name='basicauthreference_related', to='kong_admin.ConsumerReference'),
        ),
        migrations.AddField(
            model_name='apireference',
            name='owner',
            field=models.ForeignKey(related_name='infos', verbose_name='\u6240\u5c5e\u4eba', to_field=b'username', to='kong_admin.ConsumerReference', help_text='API\u6240\u5c5e\u4eba', null=True),
        ),
        migrations.AddField(
            model_name='aclreference',
            name='consumer',
            field=models.ForeignKey(related_name='aclreference_related', to='kong_admin.ConsumerReference'),
        ),
        migrations.AlterUniqueTogether(
            name='pluginconfigurationreference',
            unique_together=set([('plugin', 'api')]),
        ),
        migrations.AlterUniqueTogether(
            name='parameterreference',
            unique_together=set([('api', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='headerreference',
            unique_together=set([('api', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='errorreference',
            unique_together=set([('api', 'code')]),
        ),
    ]
