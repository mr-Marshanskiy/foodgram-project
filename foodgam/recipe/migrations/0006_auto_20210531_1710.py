# Generated by Django 3.2.3 on 2021-05-31 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20210531_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.CharField(max_length=30, verbose_name='Единицы измерений')),
            ],
            options={
                'verbose_name': 'Единица измерений',
                'verbose_name_plural': 'Единицы измерений',
                'ordering': ['measurement'],
            },
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipe.measurement', verbose_name='Единицы измерений'),
        ),
    ]