import json
from rest_framework import status, serializers
from rest_framework.test import APITestCase
from gamerraterapi.models import Game, Category, GameCategory, Rating


class GameReviewTests(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        category = Category()
        category.label = "Label"
        category.save()

        game_category = GameCategory()
        game_category.category_id = 1
        game_category.game_id = 1
        game_category.save()

    def test_review_game(self):

        game = Game()
        game.title = "Sorry"
        game.description = "Describe"
        game.designer = "Milton Bradley"
        game.year_released = 1995
        game.num_players = 10
        game.time_to_play = 60
        game.age = 12
        game.save()

        url = "/reviews"
        data = {
            "review": "Review",
            "date": "2021-11-11",
            "gameId": 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["review"], "Review")
        self.assertEqual(json_response["date"], "2021-11-11")

    def test_rate_game(self):

        game = Game()
        game.title = "Sorry"
        game.description = "Describe"
        game.designer = "Milton Bradley"
        game.year_released = 1995
        game.num_players = 10
        game.time_to_play = 60
        game.age = 12
        game.save()

        url = "/ratings"
        data = {
            "rating": 10,
            "gameId": 1,
            "playerId": 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        serializer = GameSerializer(game)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["rating"], 10)
        self.assertEqual(json_response["game"], serializer.data)

    def test_update_rating(self):

        game = Game()
        game.title = "Sorry"
        game.description = "Describe"
        game.designer = "Milton Bradley"
        game.year_released = 1995
        game.num_players = 10
        game.time_to_play = 60
        game.age = 12
        game.save()

        rating = Rating()
        rating.rating = 10
        rating.game_id = 1
        rating.player_id = 1
        rating.save()

        data = {
            "rating": 8,
            "gameId": 1,
            "playerId": 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(
            f"/ratings/{rating.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET GAME AGAIN TO VERIFY CHANGES
        response = self.client.get(f"/ratings/{rating.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the properties are correct
        self.assertEqual(json_response["rating"], 8)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer',
                  'year_released', 'num_players', 'time_to_play', 'age')
