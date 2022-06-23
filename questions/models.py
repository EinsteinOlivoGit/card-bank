from django.db import models
from django.utils import timezone

class Content(models.Model):
    content_text = models.CharField(max_length=2000)
    topic = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    state = models.CharField(max_length=2, default='AC')

    def __str__(self):
        return self.topic

class Question(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    state = models.CharField(max_length=2, default='AC')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    state = models.CharField(max_length=2, default='AC')

    def __str__(self):
        return self.choice_text

class Score(models.Model):
    nick_name = models.CharField(max_length=40)
    point = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    state = models.CharField(max_length=2, default='AC')

    def __str__(self):
        return self.nick_name.__str__() + ' score: ' + self.point.__str__()
