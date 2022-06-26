from django.urls import path
from . import views

urlpatterns = [
    path('ctopic', views.card_topic, name='ctopic'),
    path('<str:topic>', views.card, name='card'),
]
