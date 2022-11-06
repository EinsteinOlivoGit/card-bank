from django.shortcuts import render
from django.http import HttpResponse
from .models import Content
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def question_topic(request):
    contents = Content.objects.filter(state='AC')
    topic_list = map(lambda x: x.topic, contents)
    context =  {
        'topic_list': topic_list,
    }
    return render(request, 'question_topic.html', context=context)
