from django.contrib import admin
from .models import *

# Register your models here.
# class ShowLoginAdmin(admin.ModelAdmin):
#     list_display = ('id', 'human_family', 'human_name', 'human_otchestvo', 'login', 'password', 'date_create', 'date_update')
#     list_display_links = ('id', 'human_family', 'human_name', 'human_otchestvo', 'login', 'password', 'date_create', 'date_update')
#     search_fields = ('id', 'human_family', 'human_name', 'human_otchestvo', 'login', 'password', 'date_create', 'date_update')
#     list_filter = ('id', 'human_family', 'human_name', 'human_otchestvo', 'login', 'password', 'date_create', 'date_update')

# admin.site.register(Login, ShowLoginAdmin)