"""View module for handling requests about pictures"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamerraterapi.models import Picture, Player
from gamerraterapi.models.game import Game
from django.contrib.auth import get_user_model

class PictureView(ViewSet):
    """Level up pictures"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized picture instance
        """

        # Uses the token passed in the `Authorization` header
        player = Player.objects.get(user=request.auth.user)
        game = Game.objects.get(pk = request.data["game_id"])

        # Try to save the new picture to the database, then
        # serialize the picture instance as JSON, and send the
        # JSON as a response to the client request
        try:
            # Create a new Python instance of the Picture class
            # and set its properties from what was sent in the
            # body of the request from the client.
            picture = Picture.objects.create(
                url=request.data["url"],
                player=player,
                game=game
            )
            serializer = GameImageSerializer(picture, context={'request': request})

            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single picture

        Returns:
            Response -- JSON serialized picture instance
        """
        try:
            picture = Picture.objects.get(pk=pk)
            serializer = GameImageSerializer(picture, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a picture

        Returns:
            Response -- Empty body with 204 status code
        """
        player = Player.objects.get(user=request.auth.user)

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Picture, get the picture record
        # from the database whose primary key is `pk`
        picture = Picture.objects.get(pk=pk)
        picture.url = request.data["url"]
        picture.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single picture

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            picture = Picture.objects.get(pk=pk)
            picture.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Picture.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to pictures resource

        Returns:
            Response -- JSON serialized list of pictures
        """

        pictures = Picture.objects.all()
        game = self.request.query_params.get('gameId', None)
        if game is not None:
            pictures = pictures.filter(game_id__id=game)
        serializer = GameImageSerializer(
            pictures, many=True, context={'request': request})
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']


class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Player
        fields = ['user']

class GameImageSerializer(serializers.ModelSerializer):
    """JSON serializer for pictures

    Arguments:
        serializer type
    """
    player = PlayerSerializer(many=False)

    class Meta:
        model = Picture
        fields = ('id', 'url', 'player', 'game')
        depth = 1
