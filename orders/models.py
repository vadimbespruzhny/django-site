from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from my_first_site.note.models import Product

# Create your models here.


class OrderItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'

    def __str__(self):
        return f'{self.item}'

    def get_total_price(self):
        total = self.quantity * self.item.price
        return total


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,  null=True)
    last_name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    comments = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False, verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)

    def total_order_price(self):
        total = 0
        for i in self.items.all():
            total += i.get_total_price()
        return total
