from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from clients.models import People
from clients.serializers import PeopleOrderSerializer


class PeopleOrderAPIView(APIView):
    def get(self, request, people_id):
        people = People.objects.get(id=people_id)
        serializer = PeopleOrderSerializer(people)
        return Response(serializer.data, status=status.HTTP_200_OK)
