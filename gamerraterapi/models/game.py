from django.db import models

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