from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
class Number_store(models.Model):
    season=models.IntegerField()
    team1=models.CharField(max_length=50,default="")
    team2=models.CharField(max_length=50,default="")
    winner=models.CharField(max_length=50,default="")
    
    objects = UserManager()

    class Meta:
      db_table='Number_store'