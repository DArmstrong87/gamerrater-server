"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from gamerraterreports.views.helpers import dict_fetch_all


class Over5Players(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            db_cursor.execute("""
            select title as game
            FROM gamerraterapi_game
            WHERE num_players > 5
            """)

            dataset = dict_fetch_all(db_cursor)

            games_over_5_players = []

            for row in dataset:

                games_over_5_players.append({
                    'title': row['game'],
                })

        # The template string must match the file name of the html template
        template = 'games/over5players.html'

        # The context will be a dictionary that the template can access to show data
        context = {
            "over5players": games_over_5_players
        }

        return render(request, template, context)
