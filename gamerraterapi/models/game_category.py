from django.db import models

class GameCategory(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.game.title}: {self.category.label}"
