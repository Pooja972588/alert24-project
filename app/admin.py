from django.contrib import admin
from .models import Categories
from .models import News

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'image', 'description', 'date']
 

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(News, NewsAdmin)


