from django.db import models

class usersInfos(models.Model):
    FirstName  = models.CharField(max_length=20)
    LastName   = models.CharField(max_length=20)
    UserName   = models.CharField(max_length=20, unique=True)
    Email      = models.CharField(max_length=50, unique=True)
    Password   = models.CharField(max_length=50, unique=True)
    ACTIVATION = models.BooleanField(default=False)

class verificationSystem(models.Model):
    Username = models.CharField(max_length=20, unique=True)
    verCode  = models.CharField(max_length=6)