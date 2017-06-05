from django.contrib import admin

from portfolio.models import *


#
#Include ModelAdmins
#
def make_published(modeladmin, request, queryset):
    queryset.update(status='Published')
make_published.short_description = "Mark selected project module as published"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ( 'title', 'author',  'slug', 'category', 'url',  'image', 'content',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('status', 'domain', 'created_date'),
        }),
    )
    list_display = ['author', 'category', 'title', 'status', 'created_date' ]
    ordering = ['created_date']
    actions = [make_published]


