from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# CREATE TABLE Category(
#     title VARCHAR(100) UNIQUE
# );

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="articles/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):
    phone = models.CharField(max_length=255,
                             default="")
    mobile = models.CharField(max_length=255,
                             default="")
    address = models.CharField(max_length=255,
                             default="")
    job = models.CharField(max_length=255,
                             default="")
    image = models.ImageField(upload_to="profiles/",
                              null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
