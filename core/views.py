from django.shortcuts import render
from django.views.generic import ListView
from .models import Restaurant

class RestaurantListView(ListView):
    model = Restaurant
    paginate_by = 10
    template_name = 'user_site/restaurant_list.html'