from django.forms import ModelForm
from .models import Game

class GameForm(ModelForm):
    class Meta():
        model = Game
        fields = ['title', 'studio', 'description', 'amazon_url']
