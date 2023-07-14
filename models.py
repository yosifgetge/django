from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=25)
    content = models.TextField()
    price = models.IntegerField(max_length=6)
    image = models.ImageField(upload_to='photos/%y/%m/%d',)
    Active = models.BooleanField(default=True)
    def __str__(self):
        return self.name