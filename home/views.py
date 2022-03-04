from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *
from .forms import ModelForm

def fun(request):
    obj=notes.objects.all()

    return render(request,'index.html', {'results':obj,})

def details(request,notes_id):
    obj1=notes.objects.get(id=notes_id)
    return render(request,'pr.html',{'object':obj1})

def add_note(request):
    obj2=notes.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        s=notes(name=name,desc=desc,img=img)
        s.save()
        print("Note Added")
        return redirect("/")
    return render(request,"add_product.html",{'obj':obj2})


def update(request,id):
    obj=notes.objects.get(id=id)

    form=ModelForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request,'edit.html',{'form':form,'obj':obj})

def delete(request,id):
    if request.method=="POST":
        obj=notes.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')