from django.db import models

# Create your models here.


# class destination:
#     id: int
#     price: int
#     img: str
#     name: str

class destination(models.Model):
    
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to='picture')