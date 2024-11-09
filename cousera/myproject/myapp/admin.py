from django.contrib import admin
from myapp.models import Drinks, DrinksCategory, Booking, Employees

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Booking)
admin.site.register(Employees)
