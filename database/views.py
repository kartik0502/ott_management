from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import User,Content,Employee
from django.contrib import messages
from .updation import Userforms,Contentforms
# Create your views here.

def index(request):
    return render(request,"index.html")

def index1(request):
    return render(request,"insert.html")

def index2(request):
    return render(request,"view.html")

def index3(request):
    return render(request,"delete.html")

def index4(request):
    return render(request,"update.html")
  
def user_insert(request):
    if request.method == "POST":
        if request.POST.get("user_id") and request.POST.get("user_name") and request.POST.get("phone_number") and request.POST.get("email") and request.POST.get("watch_hours") and request.POST.get("employee_id"):
            emp_id = Employee.objects.get(employee_id = request.POST.get("employee_id"))
            new_obj = User(user_id=request.POST.get("user_id"),user_name=request.POST.get("user_name"),phone_number=request.POST.get("phone_number"),email=request.POST.get("email"),watch_hours=request.POST.get("watch_hours"),employee_id=emp_id)
            new_obj.save()
            messages.success(request,"The user with user ID "+request.POST.get("user_id")+" is saved successfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid Inputs")
            return render(request,'user_insert.html')
    else:
        return render(request,'user_insert.html')

def content_insert(request):
    if request.method == "POST":
        if request.POST.get("content_id") and request.POST.get("user_ratings") and request.POST.get("year_release") and request.POST.get("critics_rating") and request.POST.get("employee_id") and request.POST.get("content_name"):
            emp_id = Employee.objects.get(employee_id = request.POST.get("employee_id"))
            new_obj = Content(content_id=request.POST.get("content_id"),user_ratings=request.POST.get("user_ratings"),year_release=request.POST.get("year_release"),critics_rating=request.POST.get("critics_rating"),employee_id=emp_id,content_name=request.POST.get("content_name"))
            new_obj.save()
            messages.success(request,"The content with content ID "+request.POST.get("content_id")+" is saved successfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid Inputs")
            return render(request,'content_insert.html')
    else:
        return render(request,'content_insert.html')

def user_data(request):
    if request.method == "GET":
        p = User.objects.all().order_by('user_id').values()
        return render(request,"user_data.html",{"User":p})

def content_data(request):
    if request.method == "GET":
        p = Content.objects.all().order_by('content_id').values()
        return render(request,"content_data.html",{"Content":p})

def delete_user(request):
    if request.method == "POST":
        if request.POST.get("user_id"):
            u_id = User.objects.get(user_id = request.POST.get("user_id"))
            u_id.delete()
            messages.success(request,"The user with user ID "+request.POST.get("user_id")+" is deleted Succesfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid Inputs")
            return render(request,'delete_user.html')
    return render(request,'delete_user.html')

def delete_content(request):
    if request.method == "POST":
        if request.POST.get("content_id"):
            c_id = Content.objects.get(content_id = request.POST.get("content_id"))
            c_id.delete()
            messages.success(request,"The content with content ID "+request.POST.get("content_id")+" is deleted Succesfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid Inputs")
            return render(request,'delete_content.html')
    return render(request,'delete_content.html')


def user_update(request):
    if request.method == "POST":
        u_id = User.objects.get(user_id = request.POST.get("user_id"))
        if request.POST.get("user_name"):
            update = User.objects.get(user_id = request.POST.get("user_id"))
            form = Userforms(request.POST,instance=update)
            if form.is_valid():
                form.save()
                messages.success(request,'Record Updated Successfully')
                return redirect('/')
            else:
                messages.error(request,"Invalid Inputs")
                return render(request,'user_update.html')
        else:
            return render(request,'user_updates.html',{"User" : u_id})
    else:
        return render(request,'user_update.html')


def content_update(request):
    if request.method == "POST":
        c_id = Content.objects.get(content_id = request.POST.get("content_id"))
        if request.POST.get("content_name"):
            update = Content.objects.get(content_id = request.POST.get("content_id"))
            form = Contentforms(request.POST,instance=update)
            if form.is_valid():
                form.save()
                messages.success(request,'Record Updated Successfully')
                return redirect('/')
            else:
                messages.error(request,"Invalid Inputs")
                return render(request,'content_update.html')
        else:
            return render(request,'content_updates.html',{"Content" : c_id})
    else:
        return render(request,'content_update.html')