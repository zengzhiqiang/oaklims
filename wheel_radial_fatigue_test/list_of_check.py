from django.db import models
from .list_of_samples import Sample


class TestCheck(models.Model):
    CHECK_TAR_CHOICES = (
        ("CLSX", "车轮失效"),
        ("LTSX", "轮胎失效"),
        ("DDCS", "达到次数"),
        ("KHYQ", "客户要求"),
        ("other", "其他"),
    )
    CHECK_TORQUE_OR_PHOTO = (
        (True, "是"),
        (False, "否"),
    )
    sample_id = models.ForeignKey(Sample, on_delete=True)
    check_tag = models.CharField(max_length=5, choices=CHECK_TAR_CHOICES, default="CLSX")
    number_of_cycles = models.BigIntegerField()
    description_of_crack = models.TextField(default="无")
    torque_check = models.BooleanField(choices=CHECK_TORQUE_OR_PHOTO, default=True)
    photo_check = models.BooleanField(choices=CHECK_TORQUE_OR_PHOTO, default=True)