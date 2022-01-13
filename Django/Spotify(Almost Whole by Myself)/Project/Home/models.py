from django.db import models

# Create your models here.

class Feedback(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(default='',max_length=999)
    useremail = models.CharField(default='',max_length=999)
    feedback = models.TextField(default='',max_length=1000000)

    def __str__(self):
        return self.username + f"({self.user_id})"
