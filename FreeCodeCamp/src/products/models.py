from django.db import models

# Create your models here.

# Backend stuff
class Product(models.Model):
    # model fields
    title = models.CharField(max_length = 120) # set a text field with max size
    description = models.TextField(blank = True, null = True) # can be blank in field, allows NULL in database
    price = models.DecimalField(decimal_places = 2, max_digits = 10000) # Price has 2 decimals
    summary = models.TextField(default = 'this is cool!')
    featured = models.BooleanField() # create a new field that previous Products do not have