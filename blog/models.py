from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

from django.contrib.auth.models import AbstractUser

import uuid

# Create your models here.
ORDER_CHOICES = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('success', 'Success'),
    ('cancel', 'Cancel'),
]

class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductsModel(models.Model):
    id      =models.AutoField(primary_key=True,default=None)
    name    =models.CharField(max_length=100,default=None)
    detail  =models.TextField(default=None)    
    size    =models.CharField(max_length=100,default=None)
    quantity=models.IntegerField(default=None)
    prices  =models.IntegerField(default=None)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,default=None)
    image   =models.ImageField(default=None)
    def __str__(self):
        return self.name

class BasketModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total   =models.IntegerField(default=None)
    product =models.ForeignKey(ProductsModel,on_delete=models.CASCADE,default=None)
    user    =models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    buydate =models.DateTimeField(default=datetime.now)
    image   =models.ImageField(default=None)
    quantity=models.IntegerField(default=None)
    create_date=models.DateTimeField(default=datetime.now)

class review(models.Model):
    id      =models.AutoField(primary_key=True,default=None)
    comment = models.TextField(default=None)
    author  =models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    product =models.ForeignKey(ProductsModel,on_delete=models.CASCADE,default=None)
    time    =models.DateTimeField(default=datetime.now)



class CartModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    qty = models.IntegerField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=None)
    totalp = models.IntegerField(default=None)
    def __str__(self):
        return f"{self.qty} of {self.product.name} in cart for {self.user.username}"
    
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.JSONField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=None)
    total_qty = models.IntegerField(default=None)
    name = models.CharField(max_length=30, default=None)
    phone = models.IntegerField(default=None)
    address = models.TextField(default=None)
    status = models.CharField(max_length=20,choices=ORDER_CHOICES,default='pending')
    created_at = models.DateTimeField(default=None)
    
    def __str__(self):
        return str(self.id) 

       