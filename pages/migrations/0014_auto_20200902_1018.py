# Generated by Django 3.1 on 2020-09-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20200902_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=200),
        ),
    ]
