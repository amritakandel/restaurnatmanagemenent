from django.db import models

class Reservation(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Date=models.DateField(max_length=50)
    Time=models.TimeField(max_length=50)
    Guest=models.CharField(max_length=50)


# Create your models here.
