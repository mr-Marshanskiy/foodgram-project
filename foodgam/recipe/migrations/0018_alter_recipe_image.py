# Generated by Django 3.2.3 on 2021-06-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0017_auto_20210606_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/', verbose_name='Изображение рецепта'),
        ),
    ]