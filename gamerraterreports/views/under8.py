"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from gamerraterreports.views.helpers import dict_fetch_all


class Under8(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
            Select title
            From gamerraterapi_game
            WHERE age < 8 
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            under8 = []

            for row in dataset:

                under8.append({
                    'title': row['title']
                })

        # The template string must match the file name of the html template
        template = 'games/under8.html'

        # The context will be a dictionary that the template can access to show data
        context = {
            "under8": under8
        }

        return render(request, template, context)
