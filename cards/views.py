from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Card
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib import messages
 
TOPIC_INGLES = 'INGLES'

@login_required(login_url='login')
def card_topic(request):
    topics = Topic.objects.filter(state='AC')
    topic_list = map(lambda x: x.topic_text, topics)
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'card_topic.html', context=context)

@login_required(login_url='login')
def card(request):
    # topic = 'INGLES'
    topic = Topic.objects.get(topic_text=TOPIC_INGLES)
    card_list = Card.objects.filter(topic=topic)
    context = {
        'card': card_list[randint(0, len(card_list)-1)],
    }
    return render(request, 'card.html', context=context)

@login_required(login_url='login')
def add_card(request):

    if request.method == 'POST':
        front_text = request.POST.get('front-text')
        back_text = request.POST.get('back-text')
        print(front_text)
        print(back_text)
        if front_text and back_text:
            topic = Topic.objects.get(topic_text=TOPIC_INGLES)
            card = Card(topic=topic, front_text=front_text, back_text=back_text)
            card.save()
            messages.info(request, 'Card created successfully.')
        else:
            messages.warning(request, 'Both side of the card must have text.')


    return render(request, 'save_card.html')

