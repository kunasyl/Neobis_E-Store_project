from rest_framework import serializers

from . import models


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Order
        fields = ('id', 'user_id', 'product_id', 'product_count')
