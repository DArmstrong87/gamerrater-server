import json
from rest_framework import status
from rest_framework.test import APITestCase
from gamerraterapi.models import Game, GameCategory, Category

class GameTests(APITestCase):
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

    def test_create_game(self):
        """
        Ensure we can create a new game.
        """
        # DEFINE GAME PROPERTIES
        url = "/games"
        data = {
            "title": "Clue",
            "description": "Description",
            "designer": "Milton Bradley",
            "year_released": 1995,
            "num_players": 4,
            "time_to_play": 60,
            "age": 12,
            "categories": [1]
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["title"], "Clue")
        self.assertEqual(json_response["description"], "Description")
        self.assertEqual(json_response["designer"], "Milton Bradley")
        self.assertEqual(json_response["year_released"], 1995)
        self.assertEqual(json_response["num_players"], 4)
        self.assertEqual(json_response["time_to_play"], 60)
        self.assertEqual(json_response["age"], 12)

    def test_change_game(self):
        """
        Ensure we can change an existing game.
        """
        game = Game(pk=1)
        game.title = "Sorry"
        game.description = "Describe"
        game.designer = "Milton Bradley"
        game.year_released = 1995
        game.num_players = 10
        game.time_to_play = 60
        game.age = 12
        game.categories.set([1])
        game.save()

        # DEFINE NEW PROPERTIES FOR GAME
        data = {
            "title": "NewTitle",
            "description": "New",
            "designer": "Sorry",
            "year_released": 2000,
            "num_players": 4,
            "time_to_play": 4,
            "age": 10,
            "categories": [1]
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f"/games/{game.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET GAME AGAIN TO VERIFY CHANGES
        response = self.client.get(f"/games/{game.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the properties are correct
        self.assertEqual(json_response["title"], "NewTitle")
        self.assertEqual(json_response["description"], "New")
        self.assertEqual(json_response["designer"], "Sorry")
        self.assertEqual(json_response["year_released"], 2000)
        self.assertEqual(json_response["num_players"], 4)
        self.assertEqual(json_response["time_to_play"], 4)
        self.assertEqual(json_response["age"], 10)

    def test_delete_game(self):
        """
        Ensure we can delete an existing game.
        """
        game = Game()
        game.title = "Sorry"
        game.description = "Describe"
        game.designer = "Milton Bradley"
        game.year_released = 1995
        game.num_players = 4
        game.time_to_play = 4
        game.age = 4
        game.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f"/games/{game.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET GAME AGAIN TO VERIFY 404 response
        response = self.client.get(f"/game/{game.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_get_game(self):
        """
        Ensure we can get an existing game.
        """

        # Seed the database with a game
        game = Game()
        game.title = "Sorry"
        game.description = "Describe"
        game.designer = "Milton Bradley"
        game.year_released = 1995
        game.num_players = 4
        game.time_to_play = 60
        game.age = 10
        game.save()

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.get(f"/games/{game.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["title"], "Sorry")
        self.assertEqual(json_response["description"], "Describe")
        self.assertEqual(json_response["designer"], "Milton Bradley")
        self.assertEqual(json_response["year_released"], 1995)
        self.assertEqual(json_response["num_players"], 4)
        self.assertEqual(json_response["time_to_play"], 60)
        self.assertEqual(json_response["age"], 10)
        
    def test_get_games(self):
        
        game = Game()
        game.title = "Sorry"
        game.description = "Describe"
        game.designer = "Milton Bradley"
        game.year_released = 1995
        game.num_players = 4
        game.time_to_play = 60
        game.age = 10
        game.save()
                
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(f"/games")
        self.assertEqual(response.status_code, status.HTTP_200_OK)