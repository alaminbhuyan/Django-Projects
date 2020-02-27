from django.db import models

# Create your models here.
class employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    salary=models.IntegerField()
    status=models.BooleanField()