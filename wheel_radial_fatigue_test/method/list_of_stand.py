from django.db import models

class WhRaFaTeStand(models.Model):
    stand_code = models.CharField(max_length=128, verbose_name="标准号")   #标准号
    stand_name = models.CharField(max_length=128, verbose_name="标准名")   #标准名称
    stand_tag = models.CharField(max_length=128, verbose_name="标准标签，国标，行标，企标等")    #标签(可以是现行有效的标签或者其他)
    stand_note = models.TextField(verbose_name="备注")                 #备注

    class Meta:
        verbose_name = "标准列表"
        verbose_name_plural = "标准列表"

    def __str__(self):
        return self.stand_code + " " + self.stand_name