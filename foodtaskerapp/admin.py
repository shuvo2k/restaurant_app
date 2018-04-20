from django.contrib import admin

from foodtaskerapp.models import Resturant, Customer, Driver, Meal, Order, OrderDetails

# Register your models here.
admin.site.register(Resturant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetails)
