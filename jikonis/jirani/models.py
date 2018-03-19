from django.db import models
import datetime as dt
from django.contrib.auth.models import User

class Hood(models.Model):
    hood_name = models.CharField(max_length =30,null=True)
    hood_location = models.CharField(max_length =30, null =True)
    occupants_count = models.PositiveIntegerField(default=0)
    admin_foreign_key = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

class Commercials(models.Model):
    cover_image = models.ImageField(upload_to = 'business/', null=True, blank=True)
    business_name = models.CharField(max_length =30,null=True)
    email =  models.EmailField(max_length=70,blank=True)
    estate = models.ForeignKey(Hood,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    name = models.CharField(max_length =30,null=True)
    estate = models.ForeignKey(Hood,on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True,blank=True,)
    image_name = models.CharField(max_length=30)
    message =models.TextField(max_length = 100, null =True,blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    estate = models.ForeignKey(Hood,null =True,blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
