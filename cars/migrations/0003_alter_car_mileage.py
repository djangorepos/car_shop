# Generated by Django 4.0.5 on 2022-06-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.FloatField(),
        ),
    ]
