from django.db import models

class Content(models.Model):
    content_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    state = models.CharField(max_length=2)

class Question(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=400)
    topic = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    state = models.CharField(max_length=2)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    state = models.CharField(max_length=2)
