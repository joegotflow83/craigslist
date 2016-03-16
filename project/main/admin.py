from django.contrib import admin

from .models import UserProfile, Category, SubCategory, Post


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Post)
