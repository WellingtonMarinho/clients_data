from rest_framework import generics
from .models import People
from .serializers import PeopleSerializer


class PeopleView(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
