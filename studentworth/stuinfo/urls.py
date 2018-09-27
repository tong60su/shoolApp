#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from stuinfo import views

app_name = 'stuinfo'

urlpatterns = [
    #url(r'^report/', views.report, name='report'),网页上传成绩单，暂时不开发。
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^index/', views.index, name='index'),
    url(r'^detail/(?P<asset_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^$', views.dashboard),
]
