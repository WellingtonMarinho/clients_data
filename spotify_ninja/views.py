
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeSpotifyAPIView(APIView):
    def get(self, request):
        return Response('Hello Spotify User', status=status.HTTP_200_OK)



from ninja import NinjaAPI


api = NinjaAPI()


@api.get('/hello')
def hello(request):
    return 'Hello Spotify USER'


