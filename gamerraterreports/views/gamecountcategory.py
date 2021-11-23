"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from gamerraterreports.views.helpers import dict_fetch_all


class GameCountCategory(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            db_cursor.execute("""
            SELECT c.label category, count(*) as NumGames
            FROM gamerraterapi_category c
            JOIN gamerraterapi_gamecategory gc on c.id = gc.category_id
            JOIN gamerraterapi_game g on gc. game_id = g.id
            GROUP BY category;
            """)

            dataset = dict_fetch_all(db_cursor)

            game_count_category = []

            for row in dataset:

                game_count_category.append({
                    'label': row['category'],
                    'count': row['NumGames']
                })

        # The template string must match the file name of the html template
        template = 'games/gamecountcategory.html'

        # The context will be a dictionary that the template can access to show data
        context = {
            "gamecount": game_count_category
        }

        return render(request, template, context)
