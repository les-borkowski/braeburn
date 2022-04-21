from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from gala import views

urlpatterns = [
    path('', views.api_root),
    path('queries/', views.QueryList.as_view(), name='query-list'),
    path('queries/<int:pk>/', views.QueryDetail.as_view(), name='query-detail'),
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='users-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
