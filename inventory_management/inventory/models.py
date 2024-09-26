from django.db import models

# Create your models here.

class users(models.Model):
    id =models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=300)
    password=models.CharField(max_length=300)

