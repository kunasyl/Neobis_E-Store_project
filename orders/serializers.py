from rest_framework import serializers

from . import models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('user_id', 'product_id', 'product_count')
