from django.contrib import admin
from blogging.models import Post, Category


# Sub-classes of admin.ModelAdmin to customize how the
# corresponding models are displayed in the admin interface
class CategoryInline(admin.TabularInline):
    """
    Adds a Category element to a class of admin.ModelAdmin
    """
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    # Removes the UI element from the category admin page which allows posts to be associated with the category
    exclude = ('posts',)


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


# Registrations of DB models used by the blogging application
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
