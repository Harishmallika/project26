from django.db import models

# Create your models here.

class country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True)

class capitial(models.Model):
    capitial_name=models.ForeignKey(country,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
