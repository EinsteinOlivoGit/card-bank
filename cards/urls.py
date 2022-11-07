from django.urls import path
from . import views

urlpatterns = [
    path('ctopic', views.card_topic, name='ctopic'),
    path('', views.card, name='card'),
    path('add', views.add_card, name='add_card'),
]
