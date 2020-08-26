from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Recipe(models.Model):

    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    food_pic = models.ImageField(upload_to='recipe_pics/',blank=True,default='recipe_pics/default.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])
