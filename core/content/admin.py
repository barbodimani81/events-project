from django.contrib import admin
from django.contrib.admin import register

from .models import Event, Category, Session


class SessionInLine(admin.StackedInline):
    model = Session
    extra = 1


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_date', 'updated_date', 'status')
    list_display_links = ('id', 'title')
    list_filter = ('status', 'category', 'title')
    list_editable = ('status',)
    search_fields = ('id', 'title')
    inlines = (SessionInLine,)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_date', 'status')
    list_display_links = ('id', 'title')
    list_filter = ('status', 'title')
    list_editable = ('status',)
    search_fields = ('id', 'title')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event', 'start_time', 'end_time')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'event')
    list_editable = ('event',)
    search_fields = ('id', 'title', 'event')


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Session, SessionAdmin)
