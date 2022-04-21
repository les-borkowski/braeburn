from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gala.urls')),
    path('health/', include('health_check.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
