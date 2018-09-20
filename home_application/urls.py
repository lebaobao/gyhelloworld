# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include

urlpatterns = patterns('home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^helloworld/$', 'helloworld'),
)
