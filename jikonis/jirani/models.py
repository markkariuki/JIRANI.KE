from django.db import models
from django.contrib.auth.models import User

class Hood(models.Model):
    hood_name = models.CharField(max_length =30,null=True)
    hood_location = models.CharField(max_length =30, null =True)
    occupants_count = models.PositiveIntegerField(default=0)
    admin_foreign_key = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
