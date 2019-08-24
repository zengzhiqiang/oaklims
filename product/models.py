from django.db import models

# Create your models here.

class Product(models.Model):
    '''产品的模型'''
    part_no = models.CharField(max_length=128, verbose_name="零件号")
    part_no_customer = models.CharField(max_length=128, verbose_name="客户")
    project_name = models.CharField(max_length=128, verbose_name="项目代号")
    product_specifications = models.CharField(max_length=128, verbose_name="规格/型号")
    pitch_circle_diameter = models.CharField(max_length=128, verbose_name="PCD", default="/")
    offset = models.CharField(max_length=128, verbose_name="偏距", default="/")
    rated_load = models.CharField(max_length=128, verbose_name="额定载荷", default="/")
    vent_hole_no = models.IntegerField(verbose_name="风孔数量", default=1)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "产品列表"
        verbose_name_plural = "产品列表"