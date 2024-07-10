import pytest
from django.urls import reverse
from orders.models import Order, OrderItem
from shop.models import Product, Category

@pytest.fixture
def category():
    return Category.objects.create(name='Books', slug='books')

@pytest.fixture
def product(category):
    return Product.objects.create(
        name='Django Book',
        slug='django-book',
        category=category,
        price=20,
        available=True
    )

@pytest.fixture
def order():
    return Order.objects.create(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        address='123 Main St',
        postal_code='12345',
        city='Cityville'
    )

@pytest.fixture
def order_item(order, product):
    return OrderItem.objects.create(order=order, product=product, price=20, quantity=1)

@pytest.mark.django_db
def test_order_creation(order):
    assert order.first_name == 'John'
    assert order.last_name == 'Doe'
    assert order.email == 'john.doe@example.com'

@pytest.mark.django_db
def test_order_item_creation(order_item, product):
    assert order_item.product == product
    assert order_item.price == 20
    assert order_item.quantity == 1

@pytest.mark.django_db
def test_order_view(client, order):
    response = client.get(reverse('orders:order_create'))
    assert response.status_code == 200
    assert 'orders/order/create.html' in [t.name for t in response.templates]

