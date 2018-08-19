from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=250, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
