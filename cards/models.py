from django.db import models

class card(models.Model):
    topic = models.CharField(max_length=200)
    front_text = models.CharField(max_length=400)
    back_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    state = models.CharField(max_length=2)
