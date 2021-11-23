from django.db import models

class Review(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    review = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.game} reviewed by {self.player.first_name}"