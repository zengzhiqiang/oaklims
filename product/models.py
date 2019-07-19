from django.db import models

# Create your models here.

class Product(models.Model):
    '''产品的模型'''
    part_no = models.CharField(max_length=128)
    part_no_customer = models.CharField(max_length=128)
    project_name = models.CharField(max_length=128)
    product_specifications = models.CharField(max_length=128)