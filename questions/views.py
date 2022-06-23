from django.shortcuts import render
from django.http import HttpResponse
from .models import Content

# Create your views here.
def index(request):
    return render(request, 'index.html')

def question_topic(request):
    contents = Content.objects.filter(state='AC')
    topic_list = map(lambda x: x.topic, contents)
    context =  {
        'topic_list': topic_list,
    }
    return render(request, 'question_topic.html', context=context)
