from django.db import models
import datetime, os

# Create your models here.

class Commission(models.Model):
    commission_id = models.CharField(max_length=128)   #送检单编号
    product_id = models.CharField(max_length=128)    #产品外键，需要修改
    creat_time = models.DateTimeField(auto_now_add=True)

    def create_commission_id(self):
        '''自动生成送检单编号（导入的历史送检单不可调用该函数）'''
        if self.commission_id == "":
            try:
                filepath = os.path.join(os.path.abspath("."), "oaklims\\配置文件.txt")
                fr = open(filepath, "rw")
            except FileNotFoundError as reason:
                print("无法打开配置文件，请联系管理员！！\n%s" % str(reason))
            else:
                words = fr.readline().split("-")
                if words[0] != str(datetime.datetime.now().year) or words[1] != str(datetime.datetime.now().month):
                    self.commission_id = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month).zfill(2) + "-" + "1".zfill(3)
                else:
                    self.commission_id = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month).zfill(2) + "-" + str(int(words[3])+1).zfill(3)
                pass   #将配置写入文件需要增加
        else:
            pass