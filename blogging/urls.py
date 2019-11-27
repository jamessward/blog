"""
Blogging URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from blogging import views
from blogging.views import detail_view, list_view, stub_view
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    # Captures digits as the post_id
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),

    # From rest framework tutorial
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


