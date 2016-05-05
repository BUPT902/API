# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kongconfig/', 'kong_admin.views.show_config'),
    url(r'^api/$', 'tests.views.index'),
    url(r'^apiList/$', 'tests.views.apiList'),
    url(r'^apiCategory/(.+)/$', 'tests.views.apiCategory'),
    url(r'^apiDetail/(.+)/$', 'tests.views.apiDetail'),
    url(r'^apiFooter/', 'tests.views.apiFooter'),
    url(r'^apiHeader/', 'tests.views.apiHeader'),
    url(r'^userCenter/', 'tests.views.userCenter'),
    url(r'^registerApi/', 'tests.views.registerApi'),
    url(r'^delete_api/', 'tests.views.delete_api'),
    url(r'^apiHandler/', 'tests.views.apiHandler')
]
