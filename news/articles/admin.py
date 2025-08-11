from django.contrib import admin

# Register your models here.
from .models import Article 
class ArticleAdmin(admin.ModelAdmin):
    list_display=[
        "title",
        "body",
        "author",
    ]
admin.site.register(Article,ArticleAdmin)