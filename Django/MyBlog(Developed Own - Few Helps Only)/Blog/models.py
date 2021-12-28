from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    ref_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=199,default='')
    author = models.CharField(max_length=199,default='')
    author_story = models.TextField(default='')
    content = models.TextField(default='')
    views = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='blog/thumbnail')
    viewedBy = models.TextField(default='')
    timestamp = models.DateField(auto_now=False)

    def __str__(self):
        return 'BlogPost(' + str(self.ref_no) + ')'

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    content = models.TextField(default='')
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return 'Comment by ' + str(self.user) + str(f' ({self.sno})')