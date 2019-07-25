from django.db import models
from .list_of_samples import Sample


class TestCheck(models.Model):
    CHECK_TAR_CHOICES = (
        ("SYQ", "实验前检查"),
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
    sample_id = models.ForeignKey(Sample, on_delete=True, verbose_name="样品编号")
    check_tag = models.CharField(max_length=5, choices=CHECK_TAR_CHOICES, default="CLSX", verbose_name="检查标签")
    number_of_cycles = models.BigIntegerField(verbose_name="循环次数")
    description_of_crack = models.TextField(default="无", verbose_name="裂纹描述")
    torque_check = models.BooleanField(choices=CHECK_TORQUE_OR_PHOTO, default=True, verbose_name="扭矩是否检查")
    photo_check = models.BooleanField(choices=CHECK_TORQUE_OR_PHOTO, default=True, verbose_name="是否拍照")

    def __str__(self):
        return self.check_tag

    class Meta:
        verbose_name = "试验过程检查列表"
        verbose_name_plural = "试验过程检查列表"