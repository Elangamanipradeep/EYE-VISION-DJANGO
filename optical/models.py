from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    mobile=models.CharField(max_length=20)
    product=models.CharField(max_length=30)
    message=models.TextField()

    def __str__(self):
        return self.name
    
class Orders(models.Model):
    ProductName=models.CharField(max_length=30)
    Quantity=models.CharField(max_length=10)
    Price=models.CharField(max_length=30)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email=models.EmailField()
    Phone=models.CharField(max_length=20)
    Address=models.TextField()
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=30)

    def __str__(self):
        return self.Firstname
    
