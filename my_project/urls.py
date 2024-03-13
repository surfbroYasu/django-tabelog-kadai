from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.TopView.as_view(), name="top"),
    path("restaurants", views.RestaurantListView.as_view(), name="restaurant_list"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("logout/", views.UserLogoutView.as_view(), name="user_logout"),
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path("edit/<int:pk>", views.UserProfileUpdateView.as_view(), name="edit"),
    path("aboutus/", views.AboutUsView.as_view(), name='aboutus'),
    path("terms", views.TermsView.as_view(), name="terms"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

