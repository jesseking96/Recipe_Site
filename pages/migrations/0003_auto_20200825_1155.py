# Generated by Django 3.1 on 2020-08-25 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200825_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='food_pic',
            field=models.ImageField(blank=True, upload_to='recipe_pics/'),
        ),
    ]
