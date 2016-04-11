# Core Django imports
from django.contrib import admin

# Imports from my apps
from .models import Issue

# Register your models here.


class IssueAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['user__username', 'title']
admin.site.register(Issue, IssueAdmin)

