from django.db import models
from django import forms
class members(models.Model):
    S_no = models.IntegerField()
    FirstName = models.CharField()
    LastName = models.CharField()
    DOB = models.DateField()
    Address = models.TextField()
    Email = models.EmailField()
