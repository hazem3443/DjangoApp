from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import uuid
import os

def get_encoded_file_name(instance, filename):
    # ext = filename.split('.')[-1]
    filename = "%s" % (uuid.uuid4())
    return os.path.join('', filename)

# Create your models here.
class Customer(models.Model):
    user  = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) #whenever the user is deleted delete that relation to this customer
    name  = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to=get_encoded_file_name,default="c188345d-a2ef-4b25-9d8a-ac9137926485-default_profile_pic.svg", null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name  = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name         = models.CharField(max_length=200, null=True)
    price        = models.FloatField(null=True)
    category     = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description  = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product  = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name








