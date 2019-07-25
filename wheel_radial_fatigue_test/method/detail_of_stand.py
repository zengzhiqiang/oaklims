from django.db import models
from .list_of_stand import WhRaFaTeStand

class WhRaFaTeStandDetail(models.Model):
    CRACK_ALLOW_CHOICE = (
        (True, "允许"),
        (False, "不允许"),
    )
    wh_ra_fa_stand_id = models.ForeignKey(WhRaFaTeStand, on_delete=True, verbose_name="标准名")
    test_factor = models.FloatField(verbose_name="载荷系数")
    requirement = models.BigIntegerField(verbose_name="标准要求")
    allow_crack = models.BooleanField(choices=CRACK_ALLOW_CHOICE, verbose_name="裂纹要求")
    stand_detail_description = models.TextField(verbose_name="标准细节描述")
    stand_detail_note = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = "标准详细列表"
        verbose_name_plural = "标准详细列表"

    def __str__(self):
        return str(self.wh_ra_fa_stand_id)