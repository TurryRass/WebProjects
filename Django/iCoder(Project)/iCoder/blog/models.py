from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500,default='')
    content = models.TextField(default='')
    author = models.CharField(max_length=500,default='')
    # slug = models.CharField(max_length=130,default='')
    views = models.IntegerField(default=0)
    timestamp = models.DateTimeField(blank=True,default='')
    thumbnail = models.ImageField(upload_to = 'blog/thumbnails',default="")

    def __str__(self) -> str:
        return f'{self.title}(' + str(self.sno) + ')'

class blogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    # through the below on_delete=models.CASCADE we want to say that if the user or post is deleted then also along with it delete this comment that's it. 
    # See in user and post what actually the foreign key does is that whatever it receives from views.py of iCoder it searches for it in user table and then takes refernce from it that is we can access anything in the user (XYZ) information list like his username,first_name,second_name and so on.
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post =  models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return 'Comment(' + str(self.sno) + ')' + 'by ' + self.user.username