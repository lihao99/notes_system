import datetime
import time

from django.db import models


# Create your models here.
class Learn_Notes(models.Model):
    """"学习笔记"""
    name = models.CharField(verbose_name="标题", max_length=32)
    create_time = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)
    username = models.CharField(verbose_name="作者", max_length=32,null=True,default='')
    type_choices = (
        (1, '仅我可见'),
        (2, '所有人'),
    )
    create_type = models.IntegerField(verbose_name="发布状态", choices=type_choices,default=2)
