from django.contrib import admin
from .models import Content, Question, Choice, Score

admin.site.register(Content)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Score)
