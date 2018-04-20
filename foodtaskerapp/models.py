from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Resturant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resturant')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='resturant_logo/', blank=False)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.Case, related_name='driver')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Meal(models.Model):
    resturant = models.ForeignKey(Resturant)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='meal_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    COOKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4

    STATUS_CHOICE = (
        (COOKING,'Cooking'),
        (READY,'Ready'),
        (ONTHEWAY,'On the way'),
        (DELIVERED,'Delivered'),
    )

    customer = models.ForeignKey(Customer)
    resturant = models.ForeignKey(Resturant)
    driver = models.ForeignKey(Driver)
    address = models.CharField(max_length=500)
    total = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICE)
    treated_at = models.DateTimeField(default=timezone.now)
    picked_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_details')
    meal = models.ForeignKey(Meal)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()

    def __str__(self):
        return str(self.id)
