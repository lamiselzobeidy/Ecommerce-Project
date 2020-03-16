from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date
# Create your models here.
# -*- coding: utf-8 -*-


class Category(models.Model):
    cat_name = models.CharField(max_length=120)
    cat_id = models.IntegerField()
    cat_description = models.CharField(max_length=300)

    def __str__(self):
        return self.cat_name


class SubCategory(models.Model):
    subcat_name = models.CharField(max_length=120)
    subcat_id = models.IntegerField()
    subcat_description = models.CharField(max_length=300)

    def __str__(self):
        return self.brand_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=120)
    brand_id = models.IntegerField()
    brand_cat_id = models.IntegerField()

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    product_id = models.IntegerField()
    product_subcat_id = models.IntegerField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    image1 = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.product_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    DOB = models.DateTimeField(default=datetime.date.today, blank=True)
    location = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.user.username
