from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics')
    join_date = models.DateField(auto_now_add=True)
