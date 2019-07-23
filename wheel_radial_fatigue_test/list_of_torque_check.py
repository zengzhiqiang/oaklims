from django.db import models
from .list_of_check import TestCheck

class TorqueValue(models.Model):
    test_check_id = models.ForeignKey(TestCheck, on_delete=True)
    TorqueValue1 = models.IntegerField(default=None)
    TorqueValue2 = models.IntegerField(default=None)
    TorqueValue3 = models.IntegerField(default=None)
    TorqueValue4 = models.IntegerField(default=None)
    TorqueValue5 = models.IntegerField(default=None)
    TorqueValue6 = models.IntegerField(default=None)
    TorqueValue7 = models.IntegerField(default=None)
    TorqueValue8 = models.IntegerField(default=None)
    TorqueValue9 = models.IntegerField(default=None)
    TorqueValue10 = models.IntegerField(default=None)
    note = models.TextField(default=None)