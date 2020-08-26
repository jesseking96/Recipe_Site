from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('home')
