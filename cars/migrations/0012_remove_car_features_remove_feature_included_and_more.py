# Generated by Django 4.0.5 on 2022-06-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_car_options_feature_included_feature_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='included',
        ),
        migrations.AddField(
            model_name='car',
            name='extra_features',
            field=models.ManyToManyField(related_name='extra', to='cars.feature'),
        ),
        migrations.AddField(
            model_name='car',
            name='included_features',
            field=models.ManyToManyField(related_name='included', to='cars.feature'),
        ),
    ]
