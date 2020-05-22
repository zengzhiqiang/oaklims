from django.db import models
from .models import WhRaFaTest

class Sample(models.Model):
    wheel_radial_fatigue_test_id = models.ForeignKey(WhRaFaTest, on_delete=models.CASCADE, verbose_name="送检编号")
    sample_name = models.IntegerField(verbose_name="样品编号")

    def __str__(self):
        return self.wheel_radial_fatigue_test_id.commission_id.commission_id + "-" + str(self.sample_name)

    class Meta:
        verbose_name = "径向样品列表"
        verbose_name_plural = "径向样品列表"

    def create_samples(self, number_of_samples):
        '''
        函数未测试
        根据样品数量创建样品。
        :param number_of_samples: 客户定义的样品数量
        :return:
        '''
        for i in range(number_of_samples):
            self.sample_name = i
            self.save()