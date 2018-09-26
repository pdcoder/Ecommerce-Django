from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from ecommerce.utils import unique_slug_generator
from products.models import Products
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=120)
    
