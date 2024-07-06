from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price   = models.DecimalField( max_digits = 12, decimal_places = 2)
    desc    = models.TextField()
    image   = models.CharField(max_length=200)
    update  = models.DateTimeField(auto_now=True)
    