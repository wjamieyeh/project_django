from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:game_id>/upvote', views.upvote, name='upvote'),
    path('create/', views.create, name='create'),
    path('<int:game_id>/delete/', views.delete, name='delete'),
    path('<int:game_id>/update/', views.update, name='update'),
    # path('home/', views.igdb_get, name='igdb'),
    path('home/', views.igdb_get_ps4, name='igdb_get_ps4'),
]
