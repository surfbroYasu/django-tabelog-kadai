from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    kana = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    birthday = models.DateField()
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    occupation = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128) # ハッシュ化パスワードを格納
    subscription_active = models.BooleanField(default=False) 

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    kana = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip = models.IntegerField()
    phone = models.IntegerField()
    bottom_price = models.IntegerField()
    top_price = models.IntegerField()
    seats = models.IntegerField()

class Review(models.Model):
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
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Reservation(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reservation_for = models.DateTimeField()
    party = models.IntegerField()
  
class Like(models.Model):
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  date_added = models.DateField(auto_now_add=True)
  
class RestaurantImages(models.Model):
  image_url = models.URLField()
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  
class BusinessHours(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
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
  open_time1 = models.TimeField(null=True)
  close_time1 = models.TimeField(null=True)
  last_order1 = models.TimeField(null=True)
  open_time2 = models.TimeField(null=True)
  close_time2 = models.TimeField(null=True)
  last_order2 = models.TimeField(null=True)
  note = models.CharField(max_length=100, blank=True)  # 営業時間に関するメモ
  
class Category(models.Model):
  category_name = models.CharField(max_length=20)
  
class RestaurantCategory(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
  
class Keyword(models.Model):
  keyword = models.CharField(max_length=20)
  
class RestaurantKeyword(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
  
class Admin(models.Model):
  name = models.CharField(max_length=50)
  kana = models.CharField(max_length=50)
  email_address = models.EmailField()
  password = models.CharField(max_length=128) # ハッシュ化パスワードを格納
  
class CompanyOverview(models.Model):
  name = models.CharField(max_length=50)
  zip = models.IntegerField(max_length=15)
  address = models.CharField(max_length=50)
  management = models.CharField(max_length=50)
  date_established = models.DateField()
  capital = models.IntegerField()
  service_overview = models.TextField()
  phone_number = models.IntegerField()
  number_of_employees = models.IntegerField()
  date_updated = models.DateField(auto_now_add=True)
    
class Article(models.Model):
  content = models.TextField()
  
class Section(models.Model):
  section_number = models.IntegerField()
  description = models.TextField()
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  
class TermsOfService(models.Model):
  date_updated = models.DateField(auto_now_add=True)
  terms_overview = models.TextField()
  
  def __str__(self):
    return self.name