from rest_framework import serializers

from product.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "wine_producer",
            "country",
            "wine_name",
            "grapes",
            "description",
            "price",
            "category",
            "img",
            "active",
        ]

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)

        return product
