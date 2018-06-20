from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Game(models.Model):
    image = models.ImageField(upload_to='game_images/')
    title = models.CharField(max_length=100)
    studio = models.CharField(max_length=100)
    description = models.TextField()

    game_rater = models.ForeignKey(User, on_delete=models.CASCADE)
    # This is how we connect users to games - one to many relationship

    votes = models.IntegerField(default=1)
    amazon_url = models.URLField()
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def prettify_datetime(self):
        return self.added_date.strftime('%b %e %y')
