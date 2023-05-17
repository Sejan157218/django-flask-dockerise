from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='image',null=True)
    desc = models.TextField(max_length=500, null=True)


    def __str__(self):
            return self.title
