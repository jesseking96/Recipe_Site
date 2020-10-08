# Generated by Django 3.1 on 2020-09-02 15:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_recipe_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
    ]
