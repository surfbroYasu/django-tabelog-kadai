from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    kana = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    birthday = models.DateField()
    phone_number = PhoneNumberField(blank=True)
    email_address = models.EmailField()
    occupation = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128) # ハッシュ化パスワードを格納
    subscription_active = models.BooleanField(default=False) 

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    kana = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    phone = PhoneNumberField(blank=True)
    bottom_price = models.IntegerField()
    top_price = models.IntegerField()
    seats = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list')

class RestaurantImage(models.Model):
    image = models.ImageField(blank=True, default='noImage.png')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.restaurant

class BusinessHour(models.Model):
    name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    DAY_CHOICES = [
        ('sun', ('日曜日')),
        ('mon', ('月曜日')),
        ('tue', ('火曜日')),
        ('wed', ('水曜日')),
        ('thu', ('木曜日')),
        ('fri', ('金曜日')),
        ('sat', ('土曜日')),
    ]
    days = models.CharField(choices=DAY_CHOICES, max_length=3)
    is_closed = models.BooleanField(default=False)  # 休業の有無
    open_time = models.TimeField(default="")
    close_time = models.TimeField(default="")
    last_order = models.TimeField(default="")
    note = models.CharField(max_length=100, blank=True)  # 営業時間に関するメモ
    
    def __str__(self):
        return self.days

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    STAR_CHOICES = [
        (1, '1つ星'),
        (2, '2つ星'),
        (3, '3つ星'),
        (4, '4つ星'),
        (5, '5つ星'),
    ]
    rating = models.IntegerField(choices=STAR_CHOICES)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)
      
class Keyword(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
      
class RestaurantKeyword(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    
class Reservation(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reservation_for = models.DateTimeField()
    party = models.IntegerField()
    
    def __str__(self):
        return self.id
  
class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    date_added = models.DateField(auto_now_add=True)
    
# 運営サイト関連テーブル
class Admin(models.Model):
    name = models.CharField(max_length=50)
    kana = models.CharField(max_length=50)
    email_address = models.EmailField()
    password = models.CharField(max_length=128) # ハッシュ化パスワードを格納
  
class CompanyOverview(models.Model):
    name = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    address = models.CharField(max_length=50)
    management = models.CharField(max_length=50)
    date_established = models.DateField()
    capital = models.IntegerField()
    service_overview = models.TextField()
    phone_number = models.IntegerField()
    number_of_employees = models.IntegerField()
    date_updated = models.DateField(auto_now_add=True)

class Section(models.Model):
    section_number = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.section_number
    
class Article(models.Model):
    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.section_number
  
class TermsOfService(models.Model):
    date_updated = models.DateField(auto_now_add=True)
    terms_overview = models.TextField()
    
    def __str__(self):
        return self.name
    
