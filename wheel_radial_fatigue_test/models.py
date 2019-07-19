from django.db import models
from commissions_of_test.models import Commission

# Create your models here.

class WhRaFaTest(models.Model):
    '''
    径向送检单的模型
    '''
    #wh_ra_fa_test_id = models.CharField(max_length=128)    待定是否需要该字段
    commission_id = models.ForeignKey(Commission, on_delete=True)
    reference_standard = models.CharField(max_length=128)   #所引用的标准，外键与标准关联
    number_of_samples = models.IntegerField()
    special_requirement = models.TextField()
    note = models.TextField()
