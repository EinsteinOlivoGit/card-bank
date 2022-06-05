from datetime import time
from django.db import models
from django.utils import timezone

class Card(models.Model):
    topic = models.CharField(max_length=200)
    front_text = models.CharField(max_length=400)
    back_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    state = models.CharField(max_length=2, default='AC')

    def __str__(self):
        return self.front_text
