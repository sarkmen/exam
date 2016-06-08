from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    intro = models.TextField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    shop = models.ForeignKey(Shop)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)