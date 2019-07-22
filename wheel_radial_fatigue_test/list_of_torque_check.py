from django.db import models
from .list_of_check import TestCheck

class TorqueValue(models.Model):
    test_check_id = models.ForeignKey(TestCheck, on_delete=True)
    TorqueValue1 = models.CharField(default=None)
    TorqueValue2 = models.CharField(default=None)
    TorqueValue3 = models.CharField(default=None)
    TorqueValue4 = models.CharField(default=None)
    TorqueValue5 = models.CharField(default=None)
    TorqueValue6 = models.CharField(default=None)
    TorqueValue7 = models.CharField(default=None)
    TorqueValue8 = models.CharField(default=None)
    TorqueValue9 = models.CharField(default=None)
    TorqueValue10 = models.CharField(default=None)
    note = models.CharField(default=None)