# Generated by Django 3.1 on 2020-08-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200825_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
