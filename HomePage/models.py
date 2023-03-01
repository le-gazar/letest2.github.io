from django.db import models

# Create your models here.

class Product(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=150)
    description=models.TextField()
    image=models.ImageField()
    price=models.DecimalField(decimal_places=2, max_digits=1000)
    quantity=models.DecimalField(decimal_places=0, max_digits=10000)
    quality=models.CharField(max_length=120)
    created_at=models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category
