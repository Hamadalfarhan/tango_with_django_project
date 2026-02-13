from django.contrib import admin
from rango.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')

admin.site.register(Category, CategoryAdmin)
