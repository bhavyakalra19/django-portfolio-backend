from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    description = models.TextField(max_length=1000)
    gitImage = models.FileField(null=True, blank=True, upload_to='images/')
    gitLink = models.URLField(null=True, blank=True, verbose_name="Git Project Link")
   
    class Meta:
        verbose_name_plural = "Projects" 
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    mainImage = models.FileField(null=False, blank=False, upload_to='images/')
    created_date = models.DateField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
class ArticleData(models.Model):
    step = models.IntegerField()
    heading = models.CharField(max_length=250)
    image = models.FileField(null=True, blank=True, upload_to='images/')
    description = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="articleData")
    
    def __str__(self):
        return str(self.step) + '|' + self.article.name
    
    class Meta:
        verbose_name_plural = "Articles Data" 
    
class Skill(models.Model):
    name = models.CharField(max_length = 50)
    percentage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    logo = models.FileField(null=False, blank=False, upload_to='images/skill/')
    nightLogo = models.FileField(null=False, blank=False, upload_to='images/skill/')
    
    def __str__(self):
        return self.name