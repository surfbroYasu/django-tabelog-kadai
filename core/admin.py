from django.contrib import admin
from .models import UserProfile, Category, Restaurant, RestaurantImage, BusinessHour, Review, Keyword, RestaurantKeyword, Reservation, Like, Admin, CompanyOverview, Section, Article, TermsOfService

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(RestaurantImage)
admin.site.register(BusinessHour)
admin.site.register(Review)
admin.site.register(Keyword)
admin.site.register(RestaurantKeyword)
admin.site.register(Reservation)
admin.site.register(Like)
admin.site.register(Admin)
admin.site.register(CompanyOverview)
admin.site.register(Section)
admin.site.register(Article)
admin.site.register(TermsOfService)