from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from clients.models import People
from order.serializers import CustomerOrdersSerialiazer


class CustomerOrdersAPIView(APIView):
    serializer_class = CustomerOrdersSerialiazer

    def get(self, request, customer_uuid):
        query = People.objects.filter(id=customer_uuid)
        serializer = self.serializer_class(query, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)



class CustomerOrderAPIView(APIView):
    pass