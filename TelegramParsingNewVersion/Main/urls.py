from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path(route='', view=page_login, name='Login'),
    path(route='Quit/', view=page_quit, name='Quit'),
    path(route='Telegram/', view=page_telegram, name='Telegram'),
]