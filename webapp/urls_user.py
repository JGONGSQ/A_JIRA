# Core Django imports
from django.conf.urls import patterns, url

# Imports from my apps
from webapp import views


urlpatterns = patterns('',
                       url(r'^issue/create_edit/$', views.issue_create_edit, name='issue_create_edit'),
                       )