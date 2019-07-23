from django.db import models

class WhRaFaTeStand(models.Model):
    stand_code = models.CharField(max_length=128)   #标准号
    stand_name = models.CharField(max_length=128)   #标准名称
    stand_tag = models.CharField(max_length=128)    #标签(可以是现行有效的标签或者其他)
    stand_note = models.TextField()                 #备注
