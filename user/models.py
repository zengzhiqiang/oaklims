from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    depatment = models.CharField(max_length=128, verbose_name="部门", default="检测中心")
    cellphone = models.CharField(max_length=128, verbose_name="联系电话", default="/")