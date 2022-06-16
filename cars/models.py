from django.db import models


class Feature(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Car(models.Model):
    FUEL_TYPES = [
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric')
    ]
    image = models.ImageField()
    year = models.IntegerField()
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    body_style = models.CharField(max_length=128)
    exterior_color = models.CharField(max_length=128)
    interior_color = models.CharField(max_length=128)
    drivetrain = models.CharField(max_length=128)
    fuel_type = models.CharField(max_length=128, choices=FUEL_TYPES)
    transmission = models.CharField(max_length=128)
    engine = models.CharField(max_length=128)
    engine_displacement = models.FloatField()
    mileage = models.FloatField()
    price = models.FloatField()
    description = models.TextField()
    features = models.ManyToManyField(Feature)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.make) + ' ' + str(self.model)

    class Meta:
        ordering = ['date']
