"""A_JIRA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# Core Django imports
from django.conf.urls import include, url
from django.contrib import admin

# # Imports from apps
from webapp import views as webapp_views, urls_user

# urls at root of the project
urlpatterns = [
    # some basic urls
    url(r'^$', webapp_views.home),
    url(r'^home/$', webapp_views.home, name='home'),

    # urls for each group
    url(r'^user/', include(urls_user, namespace='user')),
    url(r'^admin/', include(admin.site.urls)),
]
