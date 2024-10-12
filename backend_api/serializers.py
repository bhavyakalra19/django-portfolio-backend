from rest_framework import serializers
from .models import Projects, ArticleData, Article, Skill

class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = '__all__'

class projectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Projects
        fields = '__all__'
        
class ArticleDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArticleData
        exclude = ['article','id']
        
class ArticleListSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Article
        fields = '__all__'
        
class ArticleSpecificSerializer(serializers.ModelSerializer):
    articleData = ArticleDataSerializer(many = True, read_only = True)
    
    class Meta:
        model = Article
        fields = '__all__'
        
class ArticleSlugSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ['slug']