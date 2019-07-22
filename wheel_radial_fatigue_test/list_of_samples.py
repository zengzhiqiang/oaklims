from django.db import models
from .models import WhRaFaTest

class Sample(models.Model):
    wheel_radial_fatigue_test_id = models.ForeignKey(WhRaFaTest, on_delete=True)


    def create_samples(self, number_of_samples):
        '''
        函数未测试
        根据样品数量创建样品。
        :param number_of_samples: 客户定义的样品数量
        :return:
        '''
        for i in range(number_of_samples):
            self.save()