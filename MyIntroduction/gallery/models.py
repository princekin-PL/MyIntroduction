from django.db import models

# Create your models here.
#创建功能模板
class Gallery(models.Model):
    #就是那个展示文本的功能，能够显示简单描述
    description = models.CharField(max_length=100)
