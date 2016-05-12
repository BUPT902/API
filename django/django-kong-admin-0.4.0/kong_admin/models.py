# -*- coding: utf-8 -*-
import logging

from six import python_2_unicode_compatible, text_type
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django_enumfield import enum
from jsonfield2 import JSONField, JSONAwareManager

from .enums import Plugins
from .validators import name_validator


# class Userinfo(models.Model):
#     userid = models.BigIntegerField(db_column='userId', primary_key=True)  # Field name made lowercase.
#     username = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.
#     password = models.CharField(max_length=255)
#     insertdate = models.DateTimeField(db_column='insertDate', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=255, blank=True, null=True)
#     apikey = models.CharField(db_column='apiKey', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hobby = models.CharField(max_length=255, blank=True, null=True)
#     profession = models.CharField(max_length=255, blank=True, null=True)
#     company = models.CharField(max_length=255, blank=True, null=True)
#     department = models.CharField(max_length=255, blank=True, null=True)
#     type = models.CharField(max_length=255, blank=True, null=True)
#     plate = models.CharField(max_length=255, blank=True, null=True)
#     url = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'userinfo'



class KongProxyModel(models.Model):
    kong_id = models.UUIDField(null=True, blank=True, editable=False)

    created_at = models.DateTimeField(u'创建于', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新于', auto_now=True)
    synchronized = models.BooleanField(default=False)
    synchronized_at = models.DateTimeField(u'同步于', null=True, blank=True, editable=False)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class APIReference(KongProxyModel):
    upstream_url = models.URLField(help_text=_(
        'The base target URL that points to your API server, this URL will be used for proxying requests. For example, '
        'https://mockbin.com.'))
    name = models.CharField(
        u'API英文名', null=True, blank=True, unique=True, max_length=32, default=None, validators=[name_validator], help_text=_(
            'The API name. If none is specified, will default to the request_host or request_path.'))
    owner = models.ForeignKey('ConsumerReference', verbose_name=u'所属人', to_field = 'username', related_name='infos', help_text=_(u'API所属人'),
                                  null=True)
    logo = models.ImageField(upload_to='image',  default='defaut.jpg', null=True, blank=True)
    dataFileName = models.CharField(u"API操作数据文件的名称", max_length=255, null=True, blank=True, help_text=u"API操作数据文件的名称")
    APIChineseName = models.CharField(u"API中文名", null=True, blank=True, max_length=32, default=None, help_text=_(
        u'请输入API的中文名'))
    request_host = models.CharField(null=True, blank=True, max_length=32, default=None, help_text=_(
        'The public DNS address that points to your API. For example, mockbin.com. At least request_host or '
        'request_path or both should be specified.'))
    request_path = models.CharField(null=True, blank=True, max_length=32, default=None, help_text=_(
        'The public path that points to your API. For example, /someservice. At least request_host or request_path or '
        'both should be specified.'))
    preserve_host = models.BooleanField(default=False, help_text=_(
        'Preserves the original Host header sent by the client, instead of replacing it with the hostname of the '
        'upstream_url. By default is false.'))
    strip_request_path = models.BooleanField(default=False, help_text=_(
        'Strip the request_path value before proxying the request to the final API. For example a request made to '
        '/someservice/hello will be resolved to upstream_url/hello. By default is false.'))
    enabled = models.BooleanField(default=True)
    API_description = models.TextField(u"API介绍", null=True, blank=True, help_text=_(u'请输入API介绍'))
    returnSample = models.TextField(u"返回样例", null=True, blank=True, help_text=_(u'请输出API的返回样例'))
    remake = models.TextField(u"备注", null=True, blank=True, help_text=_(u"请输入备注"))
    REST_METHOD_CHOICES =(
        ("1", "GET"),
        ("2", "POST"),
        ("3", "PATCH"),
        ("4", "DELETE")
    )
    APICATEGORY_CHOICES = (
        ("1", u"平台API平台数据操作"),
        ("2", u"平台API平台数据提供"),
        ("3", u"平台功能API"),
        ("4", u"外部注册API")
    )
    APIService_CHOICES = (
        ("1", u"数据操作"),
        ("2", u"生活服务"),
        ("3", u"定位服务"),
        ("4", u"交通信息"),
    )
    APIcategory = models.CharField(verbose_name=u"API类型", max_length=10, choices=APICATEGORY_CHOICES, default='1',
                                   help_text=_(u"请选择API的类型"))
    requestType = models.CharField(u"API请求类型",max_length=10, choices=REST_METHOD_CHOICES, default='1', help_text=u"请选择API的请求类型")
    APIService_category = models.CharField(u"服务类型", choices=APIService_CHOICES, default='1', max_length=10,   help_text=u"请选择API的服务类型")
    APIShort_description = models.TextField(u"API简要简介", null=True, blank=True, help_text=u"请输入API的简要介绍")
    APISecLimit = models.PositiveIntegerField(u"每秒调用峰值", default=0, help_text=u"请输入API的每秒调用峰值")
    APIDayLimit = models.PositiveIntegerField(u"每秒调用峰值", default=0, help_text=u"请输入API的每日调用峰值")


    class Meta:
        verbose_name = _(u'API')
        verbose_name_plural = _(u'API')

    def __str__(self):
        return text_type(self.upstream_url if not self.name else '%s (%s)' % (self.name, self.upstream_url))

    def clean(self):
        # if not self.request_host and not self.request_path:
        #     raise ValidationError('At least one of the parameters "request_host" and "request_path" should be set')

        if self.synchronized_at and not self.kong_id:
            raise ValidationError('There should be an kong_id parameter')

        if self.kong_id and not self.synchronized_at:
            raise ValidationError('There should be a synchronized_at parameter')


@python_2_unicode_compatible
class ParameterReference(models.Model):
    api = models.ForeignKey(APIReference, related_name='Parameter', help_text=_(
        u'请添加API的url参数'))
    name = models.CharField(u'参数名称', max_length=30)
    type = models.CharField(u'参数类型', max_length=255)
    description = models.TextField(u'参数描述', blank=True, null=True)
    defaultValue = models.CharField(u'默认值', max_length=255)
    nessesary = models.BooleanField(u'必填')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _(u'url参数')
        verbose_name_plural = _(u'url参数表')
        unique_together = (('api', 'name'),)


@python_2_unicode_compatible
class HeaderReference(models.Model):
    api = models.ForeignKey(APIReference, related_name='Header', help_text=_(
        u'请添加API的header参数'))
    name = models.CharField(_(u'参数名称'), max_length=30)
    type = models.CharField(_(u'参数类型'), max_length=255)
    description = models.TextField(_(u'参数描述'), blank=True, null=True)
    defaultValue = models.CharField(_(u'默认值'), max_length=255)
    nessesary = models.BooleanField(_(u'必填'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _(u'header参数')
        verbose_name_plural = _(u'header参数表')
        unique_together = (('api', 'name'),)


@python_2_unicode_compatible
class ErrorReference(models.Model):
    api = models.ForeignKey(APIReference, related_name='Error', help_text=_(
        u'请添加API的错误表'))
    code = models.IntegerField(u"错误码", default=0)
    message = models.CharField(u'错误信息', max_length=255)
    description = models.TextField(u'错误描述', max_length=1024)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = _(u'错误参数')
        verbose_name_plural = _(u'错误参数表')
        unique_together = (('api', 'code'), )


@python_2_unicode_compatible
class PluginConfigurationReference(KongProxyModel):
    api = models.ForeignKey(APIReference, related_name='plugins', help_text=_(
        'The API on which to add a plugin configuration'))
    consumer = models.ForeignKey('ConsumerReference', null=True, blank=True, related_name='plugins', help_text=_(
        'The consumer that overrides the existing settings for this specific consumer on incoming requests.'))
    plugin = enum.EnumField(Plugins, default=Plugins.REQUEST_SIZE_LIMITING, help_text=_(
        'The name of the Plugin that\'s going to be added. Currently the Plugin must be installed in every Kong '
        'instance separately.'))
    enabled = models.BooleanField(default=True)
    config = JSONField(default={}, help_text=_(
        'The configuration properties for the Plugin which can be found on the plugins documentation page in the '
        'Plugin Gallery.'))

    objects = JSONAwareManager(json_fields=['config'])

    class Meta:
        verbose_name = _('Plugin Configuration Reference')
        verbose_name_plural = _('Plugin Configuration References')
        unique_together = [('plugin', 'api')]

    def __str__(self):
        return text_type(Plugins.label(self.plugin))


@python_2_unicode_compatible
class ConsumerReference(KongProxyModel):
    username = models.CharField(null=True, blank=True, unique=True, max_length=32, help_text=_(
        'The username of the consumer. You must send either this field or custom_id with the request.'))
    custom_id = models.CharField(null=True, blank=True, max_length=48, help_text=_(
        'Field for storing an existing ID for the consumer, useful for mapping Kong with users in your existing '
        'database. You must send either this field or username with the request.'))
    enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = _(u'用户')
        verbose_name_plural = _(u'用户')

    def __str__(self):
        return self.username or self.custom_id

    def clean(self):
        if not self.username and not self.custom_id:
            raise ValidationError('At least one of the parameters "username" and "custom_id" should be set')


@python_2_unicode_compatible
class BuyReference(models.Model):
    consumer = models.ForeignKey(ConsumerReference, verbose_name=u'用户', related_name='Buy_consumer')
    api = models.ForeignKey(APIReference, related_name='Buy_API')
    created_at = models.DateTimeField(u'创建于', auto_now_add=True)

    class Meta:
        verbose_name = _(u'购买信息')
        verbose_name_plural = _(u'购买信息')
        unique_together = (('consumer', 'api'),)

    def __str__(self):
        return 'success'


class ConsumerAuthentication(KongProxyModel):
    consumer = models.ForeignKey(ConsumerReference, related_name="%(class)s_related",)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class BasicAuthReference(ConsumerAuthentication):
    username = models.CharField(unique=True, max_length=32, help_text=_(
        'The username to use in the Basic Authentication'))
    password = models.CharField(max_length=40, help_text=_('The password to use in the Basic Authentication'))

    class Meta:
        verbose_name = _('Basic Auth Reference')
        verbose_name_plural = _('Basic Auth References')

    def __str__(self):
        return 'BasicAuthReference(consumer: %s, username: %s)' % (self.consumer, self.username)


@python_2_unicode_compatible
class KeyAuthReference(ConsumerAuthentication):
    key = models.UUIDField(null=True, blank=True, editable=False, help_text=_(
        'You can optionally set your own unique key to authenticate the client. If missing, the plugin will generate '
        'one.'))

    class Meta:
        verbose_name = _('Key Auth Reference')
        verbose_name_plural = _('Key Auth References')

    def __str__(self):
        key = self.key
        #if len(key) > 16:
        #    key = '%s...' % key[:16]
        return 'KeyAuthReference(consumer: %s, key: %s)' % (self.consumer, key)
        


@python_2_unicode_compatible
class OAuth2Reference(ConsumerAuthentication):
    name = models.CharField(unique=True, max_length=32, help_text=_(
        'The name to associate to the credential. In OAuth 2.0 this would be the application name.'))
    redirect_uri = models.URLField(help_text=_(
        'The URL in your app where users will be sent after authorization (RFC 6742 Section 3.1.2)'))
    client_id = models.CharField(null=True, blank=True, unique=True, max_length=64, help_text=_(
        'You can optionally set your own unique client_id. If missing, the plugin will generate one.'))
    client_secret = models.TextField(null=True, blank=True, help_text=_(
        'You can optionally set your own unique client_secret. If missing, the plugin will generate one.'))

    class Meta:
        verbose_name = _('OAuth2 Reference')
        verbose_name_plural = _('OAuth2 References')

    def __str__(self):
        return 'OAuth2Reference(name: %s)' % self.name


@python_2_unicode_compatible
class AclReference(ConsumerAuthentication):
    group = models.CharField(u"用户组", unique=True, max_length=32, help_text=_(
        u'请输入用户所属的组'))

    class Meta:
        verbose_name = _('Acl Reference')
        verbose_name_plural = _('Acl References')

    def __str__(self):
        group = self.group
        #if len(key) > 16:
        #    key = '%s...' % key[:16]
        return 'AclReference(consumer: %s, group: %s)' % (self.consumer, self.group)
