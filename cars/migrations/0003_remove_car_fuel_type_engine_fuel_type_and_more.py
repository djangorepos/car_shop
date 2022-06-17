# Generated by Django 4.0.5 on 2022-06-17 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_engine_remove_car_engine_displacement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='fuel_type',
        ),
        migrations.AddField(
            model_name='engine',
            name='fuel_type',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Gasoline', 'Gasoline'), ('Hybrid', 'Hybrid')], default='Gasoline', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='standard', to='cars.engine'),
        ),
    ]
