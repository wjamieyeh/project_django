from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from . models import Game

class MyTest(TestCase):
    def setUp(self):
        print('running a test')
        self.client = Client()

    def test_get_home(self):
        user = self.make_user()
        game = self.make_game(user)
        response = self.client.get('')
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Welcome to Game Rater!")
        self.assertContains(response, game.title)

    def make_user(self):
        user = User(username="gamer_123")
        user.save()
        return user

    def make_game(self, user):
        game = Game(
            title="game title",
            studio="some studio",
            description="some description",
            game_rater=user
        )

        game.save()
        return game
