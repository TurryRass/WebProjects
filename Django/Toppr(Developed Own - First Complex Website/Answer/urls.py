from django.urls import path
from . import views

urlpatterns = [
    path('',views.ask,name = 'ask'),
    path('<int:id>/',views.do,name = 'do'),
    path('<int:id>/<str:subject_name>/',views.chapters_list,name='chapter_list'),
    path('<int:id>/<str:subject_name>/<str:chapter>/',views.questions_chapter,name='questions_chapter')
]