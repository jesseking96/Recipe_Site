from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Recipe(models.Model):

    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='recipes')
    title = models.CharField(max_length = 200,unique=True)
    description = models.TextField()
    ingredients = models.TextField(max_length=200)
    new_ingredients = ArrayField(models.CharField(max_length=200),blank=True,null=True)
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    food_pic = models.ImageField(upload_to='recipe_pics/',blank=True,default='recipe_pics/default.jpg')
    slug = models.SlugField(unique=True,null=True,blank=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    favorites = models.ManyToManyField(CustomUser,blank=True,related_name='favorite')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        return super().save()
