from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

# Create your models here.
class AttackTitan(models.Model):
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    status = models.TextField()
    ability = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MyHero(models.Model):
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    status = models.TextField()
    ability = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class JujutsuKaisen(models.Model):
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    status = models.TextField()
    ability = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

