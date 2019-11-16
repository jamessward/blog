"""
Blogging URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.urls import path
from blogging.views import stub_view

urlpatterns = [
    path('', stub_view, name="blog_index"),
]