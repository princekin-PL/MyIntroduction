from django.contrib import admin
from .models import Gallery
# Register your models here.


#每个组件创建之后都要过来激活一下
admin.site.register(Gallery)