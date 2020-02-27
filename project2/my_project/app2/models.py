from django.db import models

# Create your models here.
''' class destination:
    id: int
    name: str
    desc: str
    img: str
    price:int
    offer: bool '''


class destination(models.Model):
    
    name= models.CharField(max_length=100)
    desc= models.TextField(max_length=200)
    img= models.ImageField(upload_to='pics')
    price=models.IntegerField()
    offer= models.BooleanField(default=False)
