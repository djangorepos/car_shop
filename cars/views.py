from django.views.generic import ListView, DetailView

from cars.models import Car


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Car.objects.all()
        return context


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context
