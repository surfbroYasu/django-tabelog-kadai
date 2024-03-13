from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Restaurant, CompanyOverview, TermsOfService, Article, Section, UserProfile

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

class TopView(TemplateView):
    template_name = "user_site/top.html"

class RestaurantListView(ListView):
    template_name = 'user_site/restaurant_list.html'
    queryset = Restaurant.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurant_images'] = {}
        for restaurant in context['object_list']:
            main_image = restaurant.restaurantimage_set.filter(is_main=True).first()
            if main_image:
                context['restaurant_images'][restaurant.id] = main_image.image.url
            else:
                first_image = restaurant.restaurantimage_set.order_by('id').first()
                if first_image:
                    context['restaurant_images'][restaurant.id] = first_image.image.url
                else:
                    context['restaurant_images'][restaurant.id] = 'media_local/noImage.png'
        return context

class ReservationView():
    pass

class LikeListView(ListView):
    pass




class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "user_site/login.html"
    
class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "user_site/top.html"
    
class SignUpView(CreateView):
    template_name = "user_site/signup.html"
    model = UserProfile
    fields = '__all__'
    
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'user_site/update_account.html'
    
class AboutUsView(TemplateView):
    template_name = 'user_site/company_overview.html'
    model = CompanyOverview
    
class TermsView(TemplateView):
    template_name = 'user_site/terms_of_service.html'
    model = TermsOfService, Article, Section