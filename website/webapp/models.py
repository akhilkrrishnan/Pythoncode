from django.db import models

# Create your models here.
class Place(models.Model):
    img= models.ImageField(upload_to='pics')
    name= models.CharField(max_length=250)
    desc= models.TextField()

class People(models.Model):
        pic= models.ImageField(upload_to='pics')
        player = models.CharField(max_length=250)
        position = models.TextField()

        def __str__(self):
           return self.name
