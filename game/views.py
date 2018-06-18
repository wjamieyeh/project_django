from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'title': 'testing'})

def create(request):

    game_form = GameForm()

    return render(request, 'create.html', {
    'title':'Add a game to be Voted On',
    'game_form': game_form
    })
