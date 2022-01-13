from django.db import models

# Create your models here.
class Album(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300,default='')
    singer = models.CharField(max_length=300,null=True)
    cover = models.ImageField(upload_to = 'album/thumbnail')
    category = models.CharField(default='',max_length=100)
    description = models.TextField(default='')
    purchases = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.title) + ' by ' + str(self.singer)

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE,default='')
    sno = models.AutoField(primary_key=True)
    title = models.CharField(default='',max_length=300)
    singer = models.CharField(null=True,default='',max_length=300)
    duration = models.CharField(max_length=100,default='')
    song_file = models.FileField(upload_to='album/songs',default='')
    def __str__(self):
        return str(self.title) + (f' ({self.sno})')