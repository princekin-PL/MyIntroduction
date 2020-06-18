from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def blog_page(request):
    blogs = Blog.objects
    return render(request,'blog.html',{'blogs':blogs})

def blog_text(request,blog_id):
    #三个参数 一个是执行的CLASS 类，然后就是 blog的序号PK
    blog = get_object_or_404(Blog, pk=blog_id)
    # blogs = Blog.objects
    #第一个是请求 第二个是页面 第三个数据要用字典形式
    return render(request,'blog_text.html',{'blog':blog})
