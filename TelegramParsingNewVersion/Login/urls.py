from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path(route='', view=page_login, name='Login'),
    path(route='Telegram/', view=page_telegram, name='Telegram'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)