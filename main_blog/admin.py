from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Post) # Post entries accessible from the admin area.
admin.site.register(Category) # Category entries accessible from the admin area.