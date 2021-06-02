from django.db import models
from account.models import my_user

# Create your models here.


class Food(models.Model):
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField(blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    image = models.URLField(max_length=200, blank=False)
    veg = models.BooleanField(blank=False)


class Cart(models.Model):
    user = models.IntegerField(blank=False, null=False)
    food = models.IntegerField(blank=False, null=False)
    qty = models.IntegerField()
