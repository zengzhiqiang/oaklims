from django.db import models
from .list_of_stand import WhRaFaTeStand

class WhRaFaTeStandDetail(models.Model):
    CRACK_ALLOW_CHOICE = (
        (True, "允许"),
        (False, "不允许"),
    )
    wh_ra_fa_stand_id = models.ForeignKey(WhRaFaTeStand, on_delete=True)
    test_factor = models.FloatField()
    requirement = models.BigIntegerField()
    allow_crack = models.BooleanField(choices=CRACK_ALLOW_CHOICE)
    stand_detail_description = models.TextField()
    stand_detail_note = models.TextField()

