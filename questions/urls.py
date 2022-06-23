from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('qtopic', views.question_topic, name='qtopic'),
]
