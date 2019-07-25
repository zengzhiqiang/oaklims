from django.db import models
from .list_of_check import TestCheck

class TorqueValue(models.Model):
    '''扭矩值可为空，需要修复。'''
    test_check_id = models.ForeignKey(TestCheck, on_delete=True)
    TorqueValue1 = models.IntegerField(default=None, verbose_name="扭矩值1", blank=True)
    TorqueValue2 = models.IntegerField(default=None, verbose_name="扭矩值2", blank=True)
    TorqueValue3 = models.IntegerField(default=None, verbose_name="扭矩值3", blank=True)
    TorqueValue4 = models.IntegerField(default=None, verbose_name="扭矩值4", blank=True)
    TorqueValue5 = models.IntegerField(default=None, verbose_name="扭矩值5", blank=True)
    TorqueValue6 = models.IntegerField(default=None, verbose_name="扭矩值6", blank=True)
    TorqueValue7 = models.IntegerField(default=None, verbose_name="扭矩值7", blank=True)
    TorqueValue8 = models.IntegerField(default=None, verbose_name="扭矩值8", blank=True)
    TorqueValue9 = models.IntegerField(default=None, verbose_name="扭矩值9", blank=True)
    TorqueValue10 = models.IntegerField(default=None, verbose_name="扭矩值10", blank=True)
    note = models.TextField(default=None)

    def __str__(self):
        return self.test_check_id.sample_id.wheel_radial_fatigue_test_id.commission_id.commission_id

    class Meta:
        verbose_name = "扭矩检查列表"
        verbose_name_plural = "扭矩检查列表"