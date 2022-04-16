
from django.db import models

# Create your models here.
class subject(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=50)
    image = models.ImageField(upload_to = 'answer/ask_suject')

class TrendingChapter(models.Model):
    sno = models.AutoField(primary_key = True)
    class_no = models.IntegerField(default = 0,max_length=5)
    # below the ch is for chapter
    ch1 = models.CharField(default='', max_length=100)
    ch2 = models.CharField(default='', max_length=100)
    ch3 = models.CharField(default='', max_length=100)
    ch4 = models.CharField(default='', max_length=100)

class For_Class_Subjects(models.Model):
    sno = models.AutoField(primary_key = True)
    class_no = models.IntegerField(default = 0)
    subjects = models.CharField(default = '', max_length = 500)
    
class Chapter(models.Model):
    sno = models.AutoField(primary_key = True)
    chapters_class = models.IntegerField(default = '',max_length=10)
    subject = models.CharField(default='',max_length = 1000)
    names = models.CharField(default='',max_length=5000)

class Question(models.Model):
    sno = models.AutoField(primary_key = True)
    question_class = models.IntegerField(default = 0)
    chapter_name = models.CharField(default='',max_length=1000)
    subject = models.CharField(default='',max_length = 100)
    question = models.CharField(default = '',max_length = 1000)
    choose1 = models.CharField(default = '',max_length = 500)
    choose2 = models.CharField(default = '',max_length = 500)
    choose3 = models.CharField(default = '',max_length = 500)
    choose4 = models.CharField(default = '',max_length = 500)
    answer = models.CharField(default = '',max_length = 100)

    