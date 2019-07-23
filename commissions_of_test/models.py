from django.db import models
from product.models import Product
import datetime
import os

# Create your models here.

class Commission(models.Model):
    commission_id = models.CharField(max_length=128)   #送检单编号
    product_id = models.ForeignKey(Product, on_delete=True)
    creat_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commission_id

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

