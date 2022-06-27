from turtle import title
from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="technology")
        self.product_1 = ProductFactory(
            wine_name="mouse", price=100, category=[self.category]
        )
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEquals(serializer_data["price"], 100)
        self.assertEquals(serializer_data["wine_name"], "mouse")
        self.assertEquals(
            serializer_data["category"][0]["wine_name"], "technology")
