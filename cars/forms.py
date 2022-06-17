from django import forms
from django.forms import ModelForm

from cars.models import Car


class FilterForm(ModelForm):
    MAKES = [
        ('All makes', 'All makes'),
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
        ('All styles', 'All styles'),
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
    FUEL_TYPES = [
        ('All types', 'All types'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Gasoline', 'Gasoline'),
        ('Hybrid', 'Hybrid')
    ]
    MODELS = [
        ('All models', 'All models'),
    ]
    make = forms.ChoiceField(choices=MAKES)
    body_style = forms.ChoiceField(choices=BODY_STYLES)
    fuel_type = forms.ChoiceField(choices=FUEL_TYPES)
    model = forms.ChoiceField(choices=MODELS)

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        super().__init__()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Car
        fields = ['make', 'body_style', 'fuel_type', 'model']
