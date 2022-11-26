from django.db import models

# Create your models here.
class Administrator(models.Model):
    admin_id = models.IntegerField(primary_key = True)
    admin_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'Administrator'

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key = True)
    employee_name = models.CharField(max_length=255)
    admin_id = models.ForeignKey(Administrator,on_delete=models.CASCADE,db_column='admin_id')
    class Meta:
        db_table = 'Employee'

class User(models.Model):
    user_id = models.IntegerField(primary_key = True)
    user_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=255)
    watch_hours = models.IntegerField()
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,db_column='employee_id')
    class Meta:
        db_table = 'User'

class Subscribers(models.Model):
    subscription_id = models.IntegerField(primary_key = True)
    validity = models.DateField()
    price = models.IntegerField()
    devices_connected = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
    class Meta:
        db_table = 'Subscribers'

class Feedback(models.Model):
    feedback_id = models.IntegerField(primary_key = True)
    platform_rating = models.IntegerField()
    ads_rating = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
    class Meta:
        db_table = 'Feedback'

class Content(models.Model):
    content_id = models.IntegerField(primary_key = True)
    user_ratings = models.IntegerField()
    year_release =models.IntegerField()
    critics_rating = models.IntegerField()
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,db_column='employee_id')
    content_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'Content'

class Genre(models.Model):
    content_id = models.IntegerField()
    lang_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'Genre'

class Language(models.Model):
    content_id = models.IntegerField()
    lang_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'Language'

class Rating(models.Model):
    rating_id = models.IntegerField(primary_key = True)
    rating = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE,db_column='content_id')
    class Meta:
        db_table = 'Rating'

class Revenue(models.Model):
    revenue_id = models.IntegerField(primary_key = True)
    cost = models.IntegerField()
    budget = models.IntegerField()
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE,db_column='content_id')
    class Meta:
        db_table = 'Revenue'

class Production_House(models.Model):
    production_id = models.IntegerField()
    production_house = models.CharField(max_length=255)
    revenue = models.IntegerField()
    content_id = models.IntegerField()
    class Meta:
        db_table = 'Production_house'

class Show_type(models.Model):
    show_id = models.IntegerField()
    show_name = models.CharField(max_length=255)
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE,db_column='content_id')
    class Meta:
        db_table = 'Show_type'