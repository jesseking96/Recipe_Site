# Generated by Django 3.1 on 2020-09-02 15:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20200902_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='new_ingredients',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=200),
        ),
    ]
