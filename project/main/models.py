from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=128, null=True)


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title


class Post(models.Model):
    subcategory = models.ForeignKey(SubCategory)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="img", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=128)

    def __str__(self):
        return self.title
