from django.test import TestCase, Client
from . models import Game
from django.contrib.auth.models import User
from django.urls import reverse

new_game_title='some new title'
class CreateTest(TestCase):
    def setUp(self):
        self.user = User(username="crnpps")
        self.user.save()
        self.client = Client()

    def test_post_while_logged_in(self):
        self.client.force_login(self.user)
        self.assertEqual(self.new_game_count(), 0)

        response = self.client.post(reverse('create'), {
            'title': new_game_title,
            'studio': 'a game studio',
            'description': 'game description',
            'amazon_url': 'www.example.com'
        }, follow=True)

        self.assertEqual(self.new_game_count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Game Rater!")

        print(response)




    def new_game_count(self):
        return Game.objects.filter(title=new_game_title).count()
