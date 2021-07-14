from django.db import models
from products.models import Product


class Order(models.Model):
    CHOICES = (
        ('N', 'Новый курьер'),
        ('T', 'Ваш заказ в рассмотрении'),
        ('O', 'В дороге'),
        ('D', 'Доставлено'),
        ('С', 'Отменён'),
    )
    customer = models.ForeignKey('users.User', models.SET_NULL, related_name='customer_order', null=True)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    total_price = models.DecimalField('Цена', max_digits=10, decimal_places=0, default=0, blank=True, null=True)
    address = models.CharField('Адрес доставки', max_length=255)
    status = models.CharField(max_length=100, choices=CHOICES)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.address


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, 'product_order', null=True)
    order = models.ForeignKey(Order, models.CASCADE, related_name='product_order_product', null=True)
    quantity = models.PositiveSmallIntegerField('Количество товара', default=1)

    class Meta:
        verbose_name = 'Заказ продукта'
        verbose_name_plural = 'Заказ продуктов'
