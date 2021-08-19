from django.db import models

# Create your models here.

class crudst (models.Model):
    stname = models.CharField(max_length=200)
    stemail= models.CharField(max_length=50)
    staddress= models.CharField(max_length=100)
    stnumber= models.IntegerField()
    stgender=models.CharField(max_length=1)

