from django.urls import path
from .views import ProjectApi, ArticleListApi, ArticleSpecificApi, SkillApi, ArticleSlugPath

urlpatterns = [
    path('project-list/', ProjectApi.as_view(), name='project-api'),
    path('article-list/', ArticleListApi.as_view(), name='article-api'),
    path('article-data/<str:id>/', ArticleSpecificApi.as_view(), name="article-specific"),
    path('skills-list/', SkillApi.as_view(), name="skills-api"),
    path('artcles-slug-list/',ArticleSlugPath.as_view(), name="article-slug-list")
]