from django.conf import settings
from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path(settings.ADMIN_URL, admin.site.urls),
]
