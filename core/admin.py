from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from .models import UserProfile, Category, Restaurant, RestaurantImage, BusinessHour, Review, Keyword, RestaurantKeyword, Reservation, Like, Admin, CompanyOverview, Section, Article, TermsOfService

UserProfile = get_user_model()

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'category')
    search_fields = ('name', 'phone',)
    list_filter = ('category',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'image')
    search_fields = ('restaurant__name',)
    list_filter = ('restaurant',)
    
    def main_image(self, obj):
        main_image = obj.restaurant.restrantimage_set.filter(is_main=True).first()
        if main_image:
            return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(main_image.image.url))
        else:
            return ''

class BusinessHourAdmin(admin.ModelAdmin):
    list_display = ('days', 'name')
    search_fields = ('name',)
    
class RestaurantKeywordAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'keyword')

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'kana',)
    
class CompanyOverviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_updated')
  
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_number',)
    search_fields = ('section_number', 'description',)
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('section', 'article_number',)
  
class TermsOfServiceAdmin(admin.ModelAdmin):
    list_display = ('date_updated',)
  

admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantImage, RestaurantImageAdmin)
admin.site.register(BusinessHour, BusinessHourAdmin)
admin.site.register(Review)
admin.site.register(Keyword)
admin.site.register(RestaurantKeyword, RestaurantKeywordAdmin)
admin.site.register(Reservation)
admin.site.register(Like)
admin.site.register(Admin, AdminAdmin)
admin.site.register(CompanyOverview, CompanyOverviewAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(TermsOfService, TermsOfServiceAdmin)