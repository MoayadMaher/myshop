from django.test import TestCase
from django.urls import reverse
from .models import Category, Product

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', slug='electronics')

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            name='Smartphone',
            slug='smartphone',
            category=self.category,
            price='500',
            available=True
        )

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(self.product.__str__(), self.product.name)

class ShopViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            name='Smartphone',
            slug='smartphone',
            category=self.category,
            price='500',
            available=True
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/list.html')
        self.assertContains(response, self.product.name)

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/detail.html')
        self.assertContains(response, self.product.name)
