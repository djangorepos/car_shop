# Generated by Django 4.0.5 on 2022-06-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_rename_color_car_exterior_color_car_interior_color_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Option',
            new_name='Feature',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='extra_options',
            new_name='features',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='engine_type',
            new_name='fuel_type',
        ),
        migrations.AddField(
            model_name='car',
            name='drivetrain',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]