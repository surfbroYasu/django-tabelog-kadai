from django.contrib import admin
from .models import UserProfile, Restaurant, Review, Reservation, Like, RestaurantImages, BusinessHours

admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Reservation)
admin.site.register(Like)
admin.site.register(RestaurantImages)
admin.site.register(BusinessHours)


