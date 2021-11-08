from django.db import models
from gamerraterapi.models.rating import Rating

class Game(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    num_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="categories")

    def __str__(self):
        return self.title
    
    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = Rating.objects.filter(game=self)

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating
        avg_rating = total_rating/len(ratings)
        return avg_rating 

        # Calculate the average and return it.
        # If you don't know how to calculate average, Google it.
