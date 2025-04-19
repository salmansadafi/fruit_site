from django.db import models
from blog.models import Category

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, null=True,default='null')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email
    
class Product(models.Model):
    image = models.ImageField(upload_to='product',null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    

    def __str__(self):
        return self.title