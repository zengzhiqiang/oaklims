# Generated by Django 2.2.3 on 2019-09-01 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions_of_test', '0002_auto_20190828_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='commission_id',
            field=models.CharField(max_length=128, unique=True, verbose_name='送检编号'),
        ),
        migrations.AlterField(
            model_name='commission',
            name='test_status',
            field=models.IntegerField(choices=[(1, '待检'), (2, '已检')], default=1, verbose_name='测试状态'),
        ),
    ]
