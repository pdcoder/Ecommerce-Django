from django.db import models
from cart.models import Cart

ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('refunded','Refunded')
)
# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=120, default='created',choices=ORDER_STATUS_CHOICES)
    cart = models.ForeignKey(Cart)
    shipping_total = models.DecimalField(max_digits=100,default=5.99,decimal_places=2)
    total = models.DecimalField(max_digits=100,default=0.00,decimal_places=2)

    def __str__(self):
        return self.order_id

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id,sender=Order)