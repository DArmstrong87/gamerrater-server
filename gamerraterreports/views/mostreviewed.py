"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from gamerraterreports.views.helpers import dict_fetch_all


class MostReviewed(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            db_cursor.execute("""
            with reviewcount as (select g.title as game,
            count(*) as reviews
            FROM gamerraterapi_game g
            JOIN gamerraterapi_review r on r.game_id = g.id
            GROUP BY game)
            Select game, max(reviews) as reviews
            from reviewcount
            """)

            dataset = dict_fetch_all(db_cursor)

            most_reviewed = []

            for row in dataset:

                most_reviewed.append({
                    'game': row['game'],
                    'reviews': row['reviews'],
                })

        # The template string must match the file name of the html template
        template = 'games/mostreviewed.html'

        # The context will be a dictionary that the template can access to show data
        context = {
            "most_reviewed": most_reviewed
        }

        return render(request, template, context)
