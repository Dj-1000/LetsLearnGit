from django.contrib import admin
from .models import Article
# Register your models here.
class article_admin(admin.ModelAdmin):
    list_display = ['title','id']
    search_fields  = ['title','content']
admin.site.register(Article,article_admin)

