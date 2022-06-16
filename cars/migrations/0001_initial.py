# Generated by Django 4.0.5 on 2022-06-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('year', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('make', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('body_style', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('engine_type', models.CharField(choices=[(1, 'Benzine'), (2, 'Diesel')], max_length=128)),
                ('engine_displacement', models.FloatField()),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('extra_options', models.ManyToManyField(to='cars.option')),
            ],
        ),
    ]
