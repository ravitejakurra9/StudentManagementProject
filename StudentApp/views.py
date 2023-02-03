from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from StudentApp.models import City, Course, Student


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def reg_fun(request):
    return render(request,'register.html',{'data':''})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def regdata_fun(request):
    user_name = request.POST['txtname']
    user_email = request.POST['txtemail']
    user_password = request.POST['txtpwd']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request,'register.html',{'data':'Username or Email is already exists'})
    else:
        u1=User.objects.create_superuser(username=user_name,email=user_email,password=user_password)
        u1.save()
        return redirect('log')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def log_fun(request):
    return render(request, 'login.html',{'data':''})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def logdata_fun(request):
        user_name = request.POST['txtname']
        user_password = request.POST['txtpwd']
        user = authenticate(username=user_name,password=user_password) # if it is true it will return object otherwise None
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('home')
            else:
                return render(request,'login.html',{'data':'enter valid user name and password'})

        else:
            return render(request,'login.html',{'data':'enter valid user name and password'})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def home_fun(request):
    return render(request,'home.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def addstudent_fun(request):
    ct = City.objects.all()
    cs = Course.objects.all()

    return render(request,'addstudent.html',{'City_Data':ct,'Course_Data':cs})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def readdata_fun(request):
    s = Student()
    s.Stud_Name = request.POST['txtname']
    s.Stud_Age = int(request.POST['txtage'])
    s.Stud_Phno = int(request.POST['txtnum'])
    s.Stud_City = City.objects.get(City_Name=request.POST['ddlcity'])
    s.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
    s.save()

    return redirect('display')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def display_fun(request):
    s = Student.objects.all()
    return render(request,'display.html',{"student_data":s})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def update_fun(request,id):
    s = Student.objects.get(id=id)
    ct = City.objects.all()
    cs = Course.objects.all()
    if request.method=='POST':
        s.Stud_Name = request.POST['txtname']
        s.Stud_Age = int(request.POST['txtage'])
        s.Stud_Phno = int(request.POST['txtnum'])
        s.Stud_City = City.objects.get(City_Name=request.POST['ddlcity'])
        s.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s.save()
        return redirect('display')

    return render(request,'update.html',{'data':s,'City_Data':ct,'Course_Data':cs})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def delete_fun(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect('display')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def logout_fun(request):
    logout(request)
    return redirect('log')
