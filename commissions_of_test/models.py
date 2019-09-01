from django.db import models
from product.models import Product
import datetime
import os
from user.models import User

# Create your models here.

class TestItem(models.Model):
    test_item = models.CharField(max_length=128, verbose_name="测试项目")

    def __str__(self):
        return  self.test_item

    class Meta:
        verbose_name = "测试项目"
        verbose_name_plural = "测试项目"

class Commission(models.Model):
    TEST_STATUS_CHOICES = (
        (1, '待检'),
        (2, '已检')
    )

    commission_id = models.CharField(max_length=128, verbose_name="送检编号", unique=True)
    sample_name = models.CharField(max_length=128, verbose_name="样品名称", default="钢制车轮")
    sample_material = models.CharField(max_length=128, verbose_name="样品材料", default="/")
    sample_material_no = models.CharField(max_length=128, verbose_name="样品料号/牌号", default="/")
    sample_no = models.IntegerField(verbose_name="样品数量", default=1)
    product_id = models.ForeignKey(Product, on_delete=True, verbose_name="项目代号", default=1)
    client = models.ForeignKey(User, on_delete=True, verbose_name="联系人", default=1)
    creat_time = models.DateTimeField(auto_now_add=True, verbose_name="送检日期")
    test_item = models.ForeignKey(TestItem, on_delete=True, verbose_name="测试项目")   #外键，测试项目关联
    test_method = models.CharField(max_length=128, verbose_name="测试标准", default="GB/T5334-2005")  #外键，测试标准关联
    test_require = models.TextField(verbose_name="测试方法或条件的特殊要求说明", default="/")
    test_status = models.IntegerField(choices=TEST_STATUS_CHOICES, default=1, verbose_name="测试状态")    #测试状态
    note = models.TextField(verbose_name="备注", default="/")

    def __str__(self):
        return self.commission_id

    class Meta:
        verbose_name = "送检单列表"
        verbose_name_plural = "送检单列表"

    def create_commission_id(self):
        '''
        1、自动生成送检单编号（导入的历史送检单不可调用该函数）
        2、在送检单最后保存时需要将送检单编号写入配置文件
        '''
        if self.commission_id == "":
            try:
                filepath = os.path.join(os.path.abspath("."), "oaklims\\配置文件.txt")
                fr = open(filepath, "r")
            except FileNotFoundError as reason:
                print("无法打开配置文件，请联系管理员！！\n%s" % str(reason))
            else:
                words = fr.readline().split("-")
                if words[0] != str(datetime.datetime.now().year) or words[1] != str(datetime.datetime.now().month).zfill(2):
                    self.commission_id = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month).zfill(2) + "-" + "1".zfill(3)
                else:
                    self.commission_id = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month).zfill(2) + "-" + str(int(words[2])+1).zfill(3)
                fr.close()
        else:
            pass

    def save_me(self, commission_info):   #product作为外键后需要修改函数。
        '''
        save之前需要
        1、将送检编号存入配置文件。
        :param product:
        :return: None
        '''
        self.product_id = commission_info
        self.create_commission_id()
        self.save()
        filepath = os.path.join(os.path.abspath("."), "oaklims\\配置文件.txt")
        with open(filepath, "w") as fr:    #将当前送检单编号写入配置文件
            fr.write(self.commission_id)

    def get_year(self):
        year = self.commission_id[0:4]
        return year

    def get_month(self):
        month = self.commission_id[5:7]
        return month

    def get_number(self):
        number = self.commission_id[8:11]
        return number