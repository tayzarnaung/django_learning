from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    # def __str__(self):
    #     return '{}, {}'.format(self.name, self.price)  # return str
    #     # return self.name, self.price
    #     # will get TypeError at /pdts/
    #     # __str__ returned non-string(type tuple)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
