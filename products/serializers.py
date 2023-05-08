from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['title', 'price', 'product_image',
                  'rating', 'rating_count', 'sale']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['image', ]


# Serializer for product details
class RetrieveProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = ['id', 'title', 'price', 'description', 'category', 'product_image',
                  'rating', 'rating_count', 'sale', 'product_count', 'product_images']
