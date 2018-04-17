from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resturant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resturant')
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='resturant_logo/', blank=False)

    def __str__(self):
        return self.name
        