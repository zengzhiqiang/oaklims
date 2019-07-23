from django.db import models
from .list_of_check import TestCheck

class CheckPhoto(models.Model):
    PHOTO_TAG_CHOICES = (
        ("FMacro", "正面宏观"),
        ("FMicro", "正面微观"),
        ("BMacro", "背面宏观"),
        ("BMicro", "背面微观"),
        ("SMacro", "侧面宏观"),
        ("SMicro", "侧面微观"),
        ("Other", "其他"),
    )
    test_check_id = models.ForeignKey(TestCheck, on_delete=True)
    photo_tag = models.CharField(max_length=6, choices=PHOTO_TAG_CHOICES)
    photo = models.FileField(default=r"F:\曾志强\实验报告\照片\WeChat Image_20190722125753.png")
    description_of_photo = models.TextField(default=None)
    note_of_photo = models.TextField()


