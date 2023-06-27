from django.shortcuts import render,HttpResponse
from home.models import *
# Create your views here.
def index(request):
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        x=todo(title=title,desc=desc)
        x.save()
        alltodos=todo.objects.all()
        return render(request,'index.html',{'alltodos':alltodos})
    elif request.method=='GET':
        sno=request.GET.get('sno')
        todo.objects.filter(sno=sno).delete()
        alltodos=todo.objects.all()
        return render(request,'index.html',{'alltodos':alltodos})
    else:
        return render(request,'index.html')
sno=0 
def update(request):
    if request.method=='GET':
        global sno
        sno=request.GET.get('slno')
        return render(request,'update.html') 
    elif request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        todo.objects.filter(sno=sno).update(title=title,desc=desc)
        alltodos=todo.objects.all()
        return render(request,'index.html',{'alltodos':alltodos})
    return render(request,'update.html') 