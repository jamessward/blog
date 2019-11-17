"""
Blogging URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.urls import path
from blogging.views import detail_view, list_view, stub_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    # Captures digits as the post_id
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
