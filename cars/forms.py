from django import forms
from django.forms import ModelForm

from cars.models import Car


class FilterForm(ModelForm):
    MAKE_CHOICES = []
    MODEL_CHOICES = []
    for obj in Car.objects.all().order_by('make').distinct('make'):
        MAKE_CHOICES.append((obj.make, obj.make))
    for obj in Car.objects.all().order_by('model').distinct('model'):
        MODEL_CHOICES.append((obj.make, obj.make))

    make = forms.ChoiceField(choices=tuple(MAKE_CHOICES))
    model = forms.ChoiceField(choices=tuple(MODEL_CHOICES))

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        super().__init__()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Car
        fields = ['make', 'model']
