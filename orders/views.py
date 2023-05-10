from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from . import models, serializers, services


class OrderView(APIView):
    order = models.Order
    services = services.OrderServices()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        orders = self.services.get_orders()
        serializer = serializers.OrderSerializer(orders, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.OrderSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            valid_serializer = serializer.save()

            return Response({"success": "Article '{}' created successfully".format(valid_serializer.title)})

        return Response(serializer.errors)
