from distutils.command.upload import upload
from email.policy import default
from unicodedata import category
from django import forms
from django.db import models

# Create your models here.
class Graphic(models.Model):
    sno = models.AutoField(primary_key=True)
    category = models.CharField(default='',max_length=150)
    title = models.CharField(default='',max_length=500)
    what_text = models.CharField(default='',max_length=1000,null=True)
    for_text = models.CharField(default='',max_length=1000,null=True)
    text_color = models.CharField(default='',max_length=1000,null=True)
    default_color = models.CharField(default='',max_length=1000)
    image_color = models.CharField(default='',max_length=1000)
    for_whom_category = models.CharField(default='',max_length=1000)
    images = models.ImageField(upload_to = 'page/graphic_images',default='')

class ManyImage(models.Model):
    sno = models.AutoField(primary_key = True)
    category = models.CharField(default='',max_length=5000)
    image1 = models.ImageField(upload_to = f'many_images/category/image',default='')

    def __str__(self):
        return self.category + f"{self.sno}"
