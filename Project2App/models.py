from django.db import models
from django.utils import timezone


# Create your models here.

class NewUserModel(models.Model):
    name = models.CharField(max_length=60, default="")
    username = models.CharField(max_length=100, default="")
    password1 = models.CharField(max_length=200, default="")
    password2 = models.CharField(max_length=200, default="")

    def __str__(self):
        self.username


class WikiModel(models.Model):
    title = models.CharField(max_length=100, default="")
    body = models.TextField(max_length=3000, default="")
    date_made = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.title

    class Meta:
        abstract = True


class RelatedContentModel(models.Model):
    Title = models.CharField(max_length=100, default="")
    body = models.TextField(max_length=1000, default="")
