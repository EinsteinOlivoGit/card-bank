from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Card
from random import randint

# Create your views here.
def card_topic(request):
    topics = Topic.objects.filter(state='AC')
    topic_list = map(lambda x: x.topic_text, topics)
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'card_topic.html', context=context)

def card(request, topic):
    topic = Topic.objects.get(topic_text=topic)
    card_list = Card.objects.filter(topic=topic)
    context = {
        'card': card_list[randint(0, len(card_list)-1)],
    }
    return render(request, 'card.html', context=context)
