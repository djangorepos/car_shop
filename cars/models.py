from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Engine(models.Model):
    FUEL_TYPES = [
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Gasoline', 'Gasoline'),
        ('Hybrid', 'Hybrid')
    ]

    title = models.CharField(max_length=128)
    fuel_type = models.CharField(max_length=128, choices=FUEL_TYPES)
    displacement = models.FloatField()
    power = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Feature(models.Model):
    title = models.CharField(max_length=128)
    price = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Car(models.Model):
    MAKES = [
        ('Acura', 'Acura'),
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Buick', 'Buick'),
        ('Cadillac', 'Cadillac'),
        ('Chevrolet', 'Chevrolet'),
        ('Chrysler', 'Chrysler'),
        ('Dodge', 'Dodge'),
        ('Ford', 'Ford'),
        ('GMC', 'GMC'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('INFINITI', 'INFINITI'),
        ('Jaguar', 'Jaguar'),
        ('Jeep', 'Jeep'),
        ('Kia', 'Kia'),
        ('Land Rover', 'Land Rover'),
        ('Lexus', 'Lexus'),
        ('Lincoln', 'Lincoln'),
        ('Mazda', 'Mazda'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Nissan', 'Nissan'),
        ('Porsche', 'Porsche'),
        ('RAM', 'RAM'),
        ('Subaru', 'Subaru'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'),
    ]

    BODY_STYLES = [
        ('Cargo van', 'Cargo van'),
        ('Convertible', 'Convertible'),
        ('Coupe', 'Coupe'),
        ('Hatchback', 'Hatchback'),
        ('Minivan', 'Minivan'),
        ('Passenger van', 'Passenger van'),
        ('Pickup truck', 'Pickup truck'),
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Wagon', 'Wagon'),
    ]

    image = models.ImageField()
    year = models.IntegerField()
    make = models.CharField(max_length=128, choices=MAKES)
    model = models.CharField(max_length=128)
    body_style = models.CharField(max_length=128, choices=BODY_STYLES)
    exterior_color = models.CharField(max_length=128)
    interior_color = models.CharField(max_length=128)
    drivetrain = models.CharField(max_length=128)
    transmission = models.CharField(max_length=128)
    engine = models.ForeignKey(Engine, on_delete=models.DO_NOTHING, related_name='standard')
    compatible_engines = models.ManyToManyField(Engine, blank=True, related_name='compatible')
    mileage = models.FloatField()
    price = models.FloatField()
    description = models.TextField()
    included_features = models.ManyToManyField(Feature, related_name='included')
    extra_features = models.ManyToManyField(Feature, related_name='extra')
    date = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.make) + ' ' + str(self.model)

    class Meta:
        ordering = ['date']


class Image(models.Model):
    image = models.ImageField(upload_to='gallery')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')


class OrderedCar(models.Model):
    session_key = models.CharField(max_length=128)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='ordered_car')
    engine = models.ForeignKey(Engine, on_delete=models.DO_NOTHING, related_name='selected_engine')
    features = models.ManyToManyField(Feature, blank=True, related_name='selected_features')
    total = models.FloatField(default=0)

    def __str__(self):
        return self.session_key


class Order(models.Model):
    number = models.BigIntegerField(default=1)
    cars = models.ManyToManyField(OrderedCar, blank=True, related_name='ordered_cars')
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = PhoneNumberField()
    total = models.FloatField(default=0)
