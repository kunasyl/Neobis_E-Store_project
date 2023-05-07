from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'price', 'description', 'category',
                  'rating', 'rating_count', 'sale', 'product_count']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['image', ]


class RetrieveProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = ['id', 'title', 'price', 'description', 'category',
                  'rating', 'rating_count', 'sale', 'product_count', 'product_images']
