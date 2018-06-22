from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game
from .forms import GameForm
import json, requests, time, os
from igdb_api_python.igdb import igdb as igdb

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
            game.game_rater = request.user
            game.save()
            return redirect('home')
    else:
        game_form = GameForm()

    return render(request, 'create.html', {
    'title':'Add a game to be voted on',
    'game_form': game_form,
    })

@login_required
def upvote(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=game_id)
        game.votes += 1
        game.save()
    return redirect('home')

@login_required
def delete(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=game_id) #find the game in the db by id
        game.delete() #Deleting from the db is a cake walk!
        return redirect('profile', user_id=request.user.id)

@login_required
def update(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        update_game_form = GameForm(request.POST, instance=game)
        if update_game_form.is_valid():
            update_game_form.save()
            return redirect('profile', user_id=request.user.id)
    else:
        update_game_form = GameForm(instance=game)
    return render(request, 'update.html', {
    'title': 'Update {}'.format(game.title),
    'update_game_form':update_game_form,
    'game':game,
    })


def igdb_get_ps4(request):
    url = "https://api-endpoint.igdb.com/games/"
    querystring = {
        "fields":"*",
        "order":"rating:desc",
        "filter[platforms][eq]":"48",
        "filter[popularity][gt]":"95",
    }
    payload = "{\n        \"first_name\": \"Test\",\n        \"last_name\": \"Test\",\n        \"active\": false,\n        \"classof\": 2018\n}"
    headers = {
        'Accept': "application/json",
        'user-key': "0facb220a514493eb8c4c5129e3ef773",
        }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    if response:
        ps_games = response.json()
        # test = ps_games[0]
    # print(test)
    return render(request, 'home2.html', {'ps_games': ps_games})
