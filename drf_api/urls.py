from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


from .views import health, api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health, name="health"),
    path('api/', api, name="api"),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='docs'),
]
