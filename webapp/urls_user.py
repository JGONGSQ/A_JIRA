# Core Django imports
from django.conf.urls import patterns, url

# Imports from apps
from webapp import views


# urls at user of the project
urlpatterns = patterns('',
                       url(r'^issue/create_edit/$', views.issue_create_edit, name='issue_create_edit'),
                       )