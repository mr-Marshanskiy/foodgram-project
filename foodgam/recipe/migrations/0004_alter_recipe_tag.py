# Generated by Django 3.2.3 on 2021-05-31 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20210531_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='recipe.Tag', verbose_name='Тэги'),
        ),
    ]