from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game
from .forms import GameForm

def home(request):
    context = {
    'title':'Welcome To Game Rater',
    'games': Game.objects.order_by('-votes'),
    }
    return render(request, 'home.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        game_form = GameForm(data=request.POST)
        if game_form.is_valid():
            game = game_form.save(commit=False)
            # We'll set commit=False so we can populate our model with non model form data
            game.game_rater = request.user
            # Now we can insert the logged in user, they were attached to the request body
            game.save()
            return redirect('home')
    else:
        game_form = GameForm()

    return render(request, 'create.html', {
    'title':'Add a game to be voted on',
    'game_form': game_form,
    })
