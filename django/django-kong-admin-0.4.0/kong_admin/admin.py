# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from jsonfield2.fields import JSONField
import models
from django.contrib.admin import AdminSite

from .models import APIReference, PluginConfigurationReference, ConsumerReference, \
    BasicAuthReference, KeyAuthReference, OAuth2Reference, AclReference, \
    ParameterReference, HeaderReference, ErrorReference, \
    BuyReference
from kong_admin.views import synchronize_api_reference, synchronize_api_references, synchronize_consumer_reference, \
    synchronize_consumer_references
from .contrib import ActionButtonModelAdmin
from .widgets import JSONWidget

class MyAdminSite(AdminSite):
    site_title = u"API管理"
    site_header = u'API管理系统'
    index_title = u'API管理系统'

admin_site = MyAdminSite(name='myadmin')



def get_toggle_enable_caption(obj):
    return 'Disable' if obj.enabled else 'Enable'


class PluginConfigurationReferenceInline(admin.StackedInline):
    model = PluginConfigurationReference
    extra = 0
    fields = ('plugin', 'config', 'enabled', 'consumer')
    formfield_overrides = {
        JSONField: {'widget': JSONWidget(mode='json', width='800px', height='180px', theme='twilight')},
    }

class ParaInline(admin.StackedInline):
    model = ParameterReference
    extra = 0
    exclude = []


class HeaderInline(admin.StackedInline):
    model = HeaderReference
    extra = 0
    exclude = []


class ErrorInline(admin.StackedInline):
    model = ErrorReference
    extra = 0
    exclude = []


class APIReferenceAdmin(ActionButtonModelAdmin):
    list_display = ('upstream_url', 'name', 'APIChineseName', 'request_path', 'strip_request_path',
                    'enabled', 'synchronized', 'kong_id',)
    list_display_buttons = [{
        'caption': u'同步',
        'url': 'sync-api-ref/',
        'view': synchronize_api_reference
    }, {
        'caption': get_toggle_enable_caption,
        'url': 'toggle-enable/',
        'view': lambda request, pk: synchronize_api_reference(request, pk, toggle_enable=True)
    }]
    action_buttons = [{
        'caption': u'同步所有',
        'url': 'sync-api-refs/',
        'view': synchronize_api_references
    }]
    list_select_related = True
    # form = APIReference_Form
    fieldsets = (
        (None, {
            'fields': ('upstream_url', 'name', 'logo', 'APIChineseName', 'owner', 'APIcategory', 'requestType', 'dataFileName', 'APIService_category', 'APISecLimit', 'APIDayLimit')
        }),
        # (_('Host'), {
        #     'fields': ('request_host', 'preserve_host')
        # }),
        (_('Path'), {
            'fields': ('request_path', 'strip_request_path')
        }),
        (_('Audit'), {
            'fields': ('created_at', 'updated_at')
        }),
        (_(u'描述'), {
            'fields': ('APIShort_description', 'API_description', 'returnSample', 'remake'),
        }),
    )
    inlines = [
        ParaInline,
        HeaderInline,
        ErrorInline,
        PluginConfigurationReferenceInline,
    ]
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(APIReference, APIReferenceAdmin)
admin_site.register(APIReference, APIReferenceAdmin)

class BasicAuthInline(admin.StackedInline):
    model = BasicAuthReference
    extra = 0
    fields = ('username', 'password')


class KeyAuthInlineAdminForm(forms.ModelForm):

    def has_changed(self):
        """ Should returns True if data differs from initial.
            By always returning true even unchanged inlines will get validated and saved."""
        # return True
        return True

class KeyAuthInline(admin.StackedInline):
    form = KeyAuthInlineAdminForm
    model = KeyAuthReference
    extra = 1
    max_num = 1
    readonly_fields = ('key',)
    fields = ('key',)


class AclInline(admin.StackedInline):
    model = AclReference
    extra = 0
    fields = ('group',)


class OAuthInline(admin.StackedInline):
    model = OAuth2Reference
    extra = 0
    fields = ('name', 'redirect_uri', 'client_id', 'client_secret')


class ConsumerReferenceAdmin(ActionButtonModelAdmin):
    list_display = ('username_or_custom_id', 'enabled', 'synchronized', 'kong_id')
    list_display_buttons = [{
        'caption': u'同步',
        'url': 'sync-consumer-ref/',
        'view': synchronize_consumer_reference
    }, {
        'caption': get_toggle_enable_caption,
        'url': 'toggle-enable/',
        'view': lambda request, pk: synchronize_consumer_reference(request, pk, toggle_enable=True)
    }]
    action_buttons = [{
        'caption': u'同步所有',
        'url': 'sync-consumer-refs/',
        'view': synchronize_consumer_references
    }]
    list_select_related = True
    fieldsets = (
        (None, {
            'fields': ('username', 'custom_id', 'enabled')
        }),
        (_('Audit'), {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    inlines = [
        KeyAuthInline,
        AclInline,
    ]

    def username_or_custom_id(self, obj):
        return obj.username or obj.custom_id


# admin.site.register(ConsumerReference, ConsumerReferenceAdmin)
admin_site.register(ConsumerReference, ConsumerReferenceAdmin)

class BuyReferenceAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'api', 'created_at')
    fields = ('consumer', 'api', 'created_at')
    readonly_fields = ('created_at', )
# admin.site.register(BuyReference, BuyReferenceAdmin)
admin_site.register(BuyReference, BuyReferenceAdmin)
