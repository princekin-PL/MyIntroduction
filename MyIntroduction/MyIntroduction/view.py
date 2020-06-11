from django.shortcuts import render
from gallery.models import Gallery
def home(request):
    #调用数据库的所有那些东西
    gallerys = Gallery.objects
    return render(request,'home.html',{'gallerys':gallerys})
