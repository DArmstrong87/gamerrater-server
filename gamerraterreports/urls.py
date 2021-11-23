from django.urls import path

from gamerraterreports.views.bottom5games import Bottom5Games
from gamerraterreports.views.gamecountcategory import GameCountCategory
from gamerraterreports.views.mostreviewed import MostReviewed
from gamerraterreports.views.over5players import Over5Players
from gamerraterreports.views.under8 import Under8
from .views import Top5Games

urlpatterns = [
    path('reports/top5games', Top5Games.as_view()),
    path('reports/bottom5games', Bottom5Games.as_view()),
    path('reports/gamecountcategory', GameCountCategory.as_view()),
    path('reports/over5players', Over5Players.as_view()),
    path('reports/mostreviewed', MostReviewed.as_view()),
    path('reports/under8', Under8.as_view()),
]
