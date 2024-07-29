from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Product

class CategoryTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="TestCategory")

    def test_category_list(self):
        url = reverse('category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.category.name)

    def test_category_detail(self):
        url = reverse('category_detail', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="TestCategory")
        self.product = Product.objects.create(
            name="TestProduct",
            price=10.00,
            description="TestDescription",
            category=self.category
        )

    def test_product_list(self):
        url = reverse('product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.product.name)
        self.assertEqual(response.data[0]['price'], '10.00')
        self.assertEqual(response.data[0]['description'], self.product.description)
        self.assertEqual(response.data[0]['category'], self.category.name)

    def test_product_detail(self):
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)
        self.assertEqual(response.data['price'], '10.00')
        self.assertEqual(response.data['description'], self.product.description)
        self.assertEqual(response.data['category'], self.category.name)

