from django.db import models

# Create your models here.
#创建功能模板
class Gallery(models.Model):
    #就是那个展示文本的功能，能够显示简单描述
    description = models.CharField(default='introduce',max_length=100)
    image = models.ImageField(default='default.png',upload_to='image/')
    title = models.CharField(default='title',max_length=50)


    #这个方法可以返回一个数据库从里面才可以看见的标题
    def __str__(self):
        return self.title