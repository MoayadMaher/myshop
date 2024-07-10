# from django.test import TestCase
# from django.conf import settings
# from django.contrib.sessions.middleware import SessionMiddleware
# from django.http import HttpRequest
# from decimal import Decimal
# from shop.models import Product, Category
# from .cart import Cart

# class CartTestCase(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(name='Test Category', slug='test-category')
#         self.product = Product.objects.create(
#             category=self.category,
#             name='Test Product',
#             slug='test-product',
#             price=Decimal('10.00')
#             available=True
#         )         
#         self.request = HttpRequest()
#         self.middleware = SessionMiddleware()
#         self.middleware.process_request(self.request)
#         self.request.session.save()

#     def test_add_product_to_cart(self):
#         cart = Cart(self.request)
#         cart.add(product=self.product)
#         self.assertIn(str(self.product.id), cart.cart)
#         self.assertEqual(cart.cart[str(self.product.id)]['quantity'], 1)
















#     # def setUp(self):
#     #     self.product = Product.objects.create(
#     #         name='Test Product',
#     #         price=Decimal('10.00')
#     #     )
#     #     self.request = HttpRequest()
#     #     self.middleware = SessionMiddleware()
#     #     self.middleware.process_request(self.requt)
#     #     self.request.session.save()
    
#     # def test_add_product_to_cart(self):
#     #     cart = Cart(self.request)
#     #     cart.add(product=self.product)
#     #     self.assertIn(str(self.product.id), cart.cart)
#     #     self.assertEqual(cart.cart[str(self.product.id)]['quantity'], 1)

















#     # def test_add_product_with_quantity(self):
#     #     cart = Cart(self.request)
#     #     cart.add(product=self.product, quantity=3)
#     #     self.assertEqual(cart.cart[str(self.product.id)]['quantity'], 3)

#     # def test_remove_product_from_cart(self):
#     #     cart = Cart(self.request)
#     #     cart.add(product=self.product)
#     #     cart.remove(self.product)
#     #     self.assertNotIn(str(self.product.id), cart.cart)

#     # def test_iter_cart(self):
#     #     cart = Cart(self.request)
#     #     cart.add(product=self.product, quantity=2)
#     #     items = list(cart)
#     #     self.assertEqual(len(items), 1)
#     #     self.assertEqual(items[0]['product'], self.product)
#     #     self.assertEqual(items[0]['quantity'], 2)

#     # def test_cart_length(self):
#     #     cart = Cart(self.request)
#     #     cart.add(product=self.product, quantity=3)
#     #     self.assertEqual(len(cart), 3)

#     # def test_get_total_price(self):
#     #     cart = Cart(self.request)
#     #     cart.add(product=self.product, quantity=2)
#     #     expected_total = Decimal('20.00')
#     #     self.assertEqual(cart.get_total_price(), expected_total)

#     # def test_clear_cart(self):
#     #     cart = Cart(self.request)
#     #     cart.add(product=self.product)
#     #     cart.clear()
#     #     self.assertEqual(len(cart.cart), 0)