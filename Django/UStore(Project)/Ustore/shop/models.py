from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField

# Create your models here.
class Product(models.Model): 
    # here model is a class itself
    product_id = models.AutoField # here near AutoField there (primary_key = True)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    publishDate = models.DateField()
    Category = models.CharField(max_length=50 , default="")
    SubCategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    Image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model): 
    # here model is a class itself
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70,default='')
    email = models.CharField(max_length=80,default='')
    phNumber = models.CharField(max_length=15,default='')
    desc = models.CharField(max_length=500,default='')
    def __str__(self):
        return 'Contact ' + str(self.userId)

class Order(models.Model): 
    # here model is a class itself
    itemsJson = models.CharField(max_length=5000,default='')
    OrderId = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=150,default='')
    email = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=100,default='')
    state = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=15,default='')
    zipCode = models.CharField(max_length=15,default='')
    def __str__(self):
        return 'Order ' + str(self.OrderId)

class orderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=500)
    timestamp = models.DateField(auto_now_add=True) # gives now time if not given something other.

    def __str__(self):
        return self.update_desc[0:11] + '...'
    
    