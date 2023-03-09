from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # includes api/urls.py file for urls instructions
    path('', include('api.urls')),
]
