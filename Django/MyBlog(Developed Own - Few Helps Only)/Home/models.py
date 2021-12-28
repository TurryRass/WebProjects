from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class Contact(models.Model):
    ref_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default='')
    email = models.EmailField(max_length=500,default='')
    password = models.CharField(max_length=200,default='')
    text = models.TextField(default='')

    def __str__(self):
        return self.name + f'({self.ref_id})'

