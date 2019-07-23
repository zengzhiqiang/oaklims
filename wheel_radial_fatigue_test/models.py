from django.db import models
from commissions_of_test.models import Commission
from .method.detail_of_stand import WhRaFaTeStandDetail

# Create your models here.

class WhRaFaTest(models.Model):
    '''
    径向送检单的模型
    '''
    #wh_ra_fa_test_id = models.CharField(max_length=128)    待定是否需要该字段
    commission_id = models.ForeignKey(Commission, on_delete=True)
    standard_more = models.ForeignKey(WhRaFaTeStandDetail, on_delete=True)   #与所引用标准的细节相关联，载荷系数。
    number_of_samples = models.IntegerField()
    special_requirement = models.TextField()
    note = models.TextField()

    def __str__(self):
        return self.commission_id