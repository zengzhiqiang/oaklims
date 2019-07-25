from django.db import models
from commissions_of_test.models import Commission
from .method.list_of_stand import WhRaFaTeStand
from .method.detail_of_stand import WhRaFaTeStandDetail

# Create your models here.

class WhRaFaTest(models.Model):
    '''
    径向送检单的模型
    '''
    #wh_ra_fa_test_id = models.CharField(max_length=128)    待定是否需要该字段
    commission_id = models.ForeignKey(Commission, on_delete=True, verbose_name="送检编号")
    standard_more = models.ForeignKey(WhRaFaTeStandDetail, on_delete=True, verbose_name="标准详情")   #与所引用标准的细节相关联，载荷系数。
    number_of_samples = models.IntegerField(verbose_name="样品数量")
    special_requirement = models.TextField(verbose_name="特殊要求")
    note = models.TextField(verbose_name="备注")

    class Meta:
        unique_together = ("commission_id", "standard_more")
        verbose_name = "径向试验列表"
        verbose_name_plural = "径向试验列表"

    def __str__(self):
        #print(self.commission_id.commission_id)
        #print(type(self.commission_id.commission_id))
        return self.commission_id.commission_id
