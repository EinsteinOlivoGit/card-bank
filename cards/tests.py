from django.test import TestCase
from .models import Card, Topic

# Create your tests here.
class CaseTestCase(TestCase):
    def setUp(self):
        topic_italiano = Topic.objects.create(topic_text='Italiano')
        Card.objects.create(topic=topic_italiano, front_text='Mama mia!', back_text='Madre mia!')

    def test_card(self):
        card = Card.objects.get(front_text='Mama mia!')
        self.assertEqual(card.back_text, 'Madre mia!')
