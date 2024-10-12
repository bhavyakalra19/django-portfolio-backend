from django.shortcuts import render
from rest_framework.response import Response
from .models import Projects, Article, ArticleData, Skill
from rest_framework import status, generics
from .serializers import projectSerializer, ArticleListSerializer, ArticleSpecificSerializer, SkillSerializer, ArticleSlugSerializer
from django.db.models import Prefetch
from rest_framework.views import APIView
import backend_api.HelperFile as HelperFile
    
    
class ArticleListApi(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    
        
class ArticleSpecificApi(generics.ListAPIView):
    serializer_class = ArticleSpecificSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        try:
            article = Article.objects.get(slug = id)
        except Article.DoesNotExist:
            return None
        return Article.objects.prefetch_related(Prefetch("articleData",queryset=ArticleData.objects.filter(article = article).order_by('step'))).filter(slug = id)
        
        
class SkillApi(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
    
class ProjectApi(APIView):
    
    def get(self, request):
        # if(request.GET):
        #     print(request.GET.get('check'))
        projects_featured = Projects.objects.filter(featured = True)
        projects_non_featured = Projects.objects.filter(featured = False)
        
        serializer_featured = projectSerializer(projects_featured, many = True)
        serializer_non_featured = projectSerializer(projects_non_featured, many = True)
        helper = HelperFile.HelperClass()
        data = helper.sortProjectData(serializer_featured.data, serializer_non_featured.data)
        return Response(data)
    
    
class ArticleSlugPath(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSlugSerializer