# rest_project1/urls.py
from django.contrib import admin
from django.urls import path, include
from api import urls as api_urls  # import api urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include(api_urls)),
    # other url patterns
]
