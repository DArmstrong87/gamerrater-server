from django.db import models

class Rating(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.game} rated {self.rating} by {self.player}"