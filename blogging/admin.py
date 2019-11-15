from django.contrib import admin
from blogging.models import Post, Category

# Registrations of DB models used by the blogging application
admin.site.register(Post)
admin.site.register(Category)
