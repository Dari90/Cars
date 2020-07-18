from django.shortcuts import render
from .models import Cars
from django.views.generic import ListView
from django.db.models import Q


class CarList(ListView):
    model = Cars
    template_name = 'index.html'

    def get_queryset(self):
        if 'Search' in self.request.GET:
            query = self.request.GET.get('search', '')
            flag = False
            if query == 'Механика':
                query = 1
                flag = True
            elif query == 'Автомат':
                query = 2
                flag = True
            elif query == 'Робот':
                query = 3
                flag = True
            if flag:
                cars_list = Cars.objects.filter(
                    transmission=query)
            else:
                cars_list = Cars.objects.filter(
                    Q(manufacturer__icontains=query)|
                    Q(model__icontains=query)|
                    Q(release_year__icontains=query)|
                    Q(colors__icontains=query))
            return cars_list
        return Cars.objects.all()
