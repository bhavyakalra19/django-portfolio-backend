from django.contrib import admin
from .models import Projects, Article, ArticleData, Skill

# Register your models here.
admin.site.register(Projects)
admin.site.register(Article)
admin.site.register(ArticleData)
admin.site.register(Skill)