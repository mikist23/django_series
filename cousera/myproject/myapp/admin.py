from django.contrib import admin
from myapp.models import Drinks, DrinksCategory, Booking

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Booking)
