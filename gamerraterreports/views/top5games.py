"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from gamerraterreports.views.helpers import dict_fetch_all


class Top5Games(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
            Select
            g.title,
            r.rating rating
            from gamerraterapi_game g
            JOIN gamerraterapi_rating r on g.id = r.game_id
            ORDER BY rating desc
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            games_by_rating = []

            for row in dataset:

                games_by_rating.append({
                    'title': row['title'],
                    'rating': row['rating']
                })

        # The template string must match the file name of the html template
        template = 'games/top5games.html'

        # The context will be a dictionary that the template can access to show data
        context = {
            "top5games": games_by_rating
        }

        return render(request, template, context)
