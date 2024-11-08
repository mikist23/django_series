from django.db import models

# Create your models here.

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    prices = models.IntegerField()
    

    def __str__(self):
        return super().__str__()