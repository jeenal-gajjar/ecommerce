from django.db import models
from ecommerce.app.inventory.models import Product


# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    phone_number = models.CharField(max_length=250, null=True)
    shipping_address = models.CharField(max_length=250, null=True)
    tracking_number = models.CharField(max_length=250, null=True)
    received_date = models.DateTimeField(auto_now_add=True)
    total_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='order_for_order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_for_order_item')
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)
