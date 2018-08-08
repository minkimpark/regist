from django.db import models

class member(models.Model):
    num = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    joindate = models.DateField(null=True,blank=True)


class board(models.Model):
    num =models.IntegerField(primary_key=True)
    id=models.CharField(max_length=25)
    subject = models.CharField(max_length=100)
    content = models.CharField(max_length=20000)
    writedate = models.DateField(null=True,blank=True)
    hits= models.IntegerField(null=True,blank=True)
