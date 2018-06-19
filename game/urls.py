from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:game_id>/upvote', views.upvote, name='upvote'),
    path('create/', views.create, name='create'),
]
