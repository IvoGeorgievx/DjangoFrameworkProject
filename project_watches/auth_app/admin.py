from django.contrib import admin

from project_watches.auth_app.models import Profile, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    ordering = ('first_name', 'last_name',)
    list_filter = ('first_name', 'last_name',)
    search_fields = ('first_name__startswith', 'last_name__startswith',)
    list_per_page = 3


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')
    ordering = ('email', 'name')
    list_filter = ('email', 'name')
    search_fields = ('description__startswith', 'email__startswith', 'name__startswith')
    list_per_page = 3
