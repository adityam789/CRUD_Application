from django.shortcuts import render
from CRUD.models import crudst
from django.contrib import messages
from CRUD.forms import stform

# Create your views here.
def stdisplay(request):
    results=crudst.objects.all()
    return render(request,'index.html',{"crudst":results})

def stinsert(request):
    if request.method=="POST":
        if request.POST.get("stname") and request.POST.get("stemail") and request.POST.get("staddress") and request.POST.get("stnumber") and request.POST.get("stnumber") and request.POST.get("stgender"):
            savest=crudst()
            savest.stname=request.POST.get("stname")
            savest.stemail=request.POST.get("stemail")
            savest.staddress=request.POST.get("staddress")
            savest.stnumber=request.POST.get("stnumber")
            savest.stgender=request.POST.get("stgender")
            savest.save()
            messages.success(request,"The Record "+savest.stname+" has been successfully created..!")
            return render(request,"create.html")
    else:
        return render(request,"create.html")

def stedit(request,id):
    getstudentdetails=crudst.objects.get(id=id)
    return render(request,'edit.html',{"crudst":getstudentdetails})

def stupdate(request,id):
    stupdate=crudst.objects.get(id=id)
    form=stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The student Record is updated successfully")
        return render(request,"edit.html",{"crudst":stupdate})

def stdel(request,id):
    delstudent=crudst.objects.get(id=id)
    delstudent.delete()
    results=crudst.objects.all()
    return render(request,'index.html',{"crudst":results})



