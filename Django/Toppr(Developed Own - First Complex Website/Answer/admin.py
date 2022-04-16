from django.contrib import admin

from .models import Question, subject,TrendingChapter,For_Class_Subjects,Chapter

# Register your models here.
admin.site.register(subject)
admin.site.register(TrendingChapter)
admin.site.register(For_Class_Subjects)
admin.site.register(Chapter)
admin.site.register(Question)
