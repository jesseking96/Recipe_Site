# Generated by Django 3.1 on 2020-08-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200825_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='food_pic',
            field=models.ImageField(blank=True, default='recipe_pics/default.jpg', upload_to='recipe_pics/'),
        ),
    ]
