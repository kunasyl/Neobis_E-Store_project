from rest_framework import serializers

from . import models


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ('user_id', )


# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CartItem
#         fields = ('product_id', )


# class RetrieveCartSerializer(serializers.ModelSerializer):
#     cart_items =