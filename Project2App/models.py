from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class NewUserModel(models.Model):
    name = models.CharField(max_length=60, default="")
    username = models.CharField(max_length=100, default="", unique=True)
    password1 = models.CharField(max_length=200, default="")
    password2 = models.CharField(max_length=200, default="")
    userForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class BaseModel(models.Model):
    date_made = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WikiModel(BaseModel):
    title = models.CharField(max_length=100, default="")
    body = models.TextField(max_length=3000, default="")
    image = models.ImageField(upload_to='site_media/', default='site_media/None/no-img.jpg')
    wikiForeignKey = models.ForeignKey(NewUserModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class RelatedContentModel(models.Model):
    Title = models.CharField(max_length=100, default="")
    body = models.TextField(max_length=1000, default="")
    image = models.ImageField(upload_to='site_media/', default='site_media/None/no-img.jpg')
    relatedForeignKey = models.ForeignKey(WikiModel, on_delete=models.SET_NULL, null=True, blank=True)
