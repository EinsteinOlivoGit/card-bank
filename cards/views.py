from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic

# Create your views here.
def card_topic(request):
    topics = Topic.objects.filter(state='AC')
    topic_list = map(lambda x: x.topic_text, topics)
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'card_topic.html', context=context)
