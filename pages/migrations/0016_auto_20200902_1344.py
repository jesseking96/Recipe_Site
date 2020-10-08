# Generated by Django 3.1 on 2020-09-02 18:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0015_recipe_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]