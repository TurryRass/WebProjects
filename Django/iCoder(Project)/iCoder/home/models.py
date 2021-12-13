from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=13,default='')
    content = models.TextField(max_length=1000,default='')
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self) -> str:
        return 'username' + str(self.sno)