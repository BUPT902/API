# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from django.conf.urls import include, url
from django.contrib import admin
import os
BASE_DIR2 = os.path.dirname(os.path.dirname(__file__))


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
    url(r'^modifyApi/(.+)/$', 'tests.views.modifyApi'),
    url(r'^delete_api/', 'tests.views.delete_api'),
    url(r'^apiHandler/', 'tests.views.apiHandler'),
    url(r'^registerConsumer$', 'tests.views.registerConsumer'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(BASE_DIR2,'media'), 'show_indexes': True }),
]