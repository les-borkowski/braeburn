from django.contrib import admin
from django.urls import path
from .views import health, api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health, name="health"),
    path('api/', api, name="api")
]
