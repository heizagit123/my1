from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from .models import application



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST.get('password1')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();

                return redirect('login')

        else:
            messages.info(request,"password not matched")
            return redirect('apply')
        return redirect('/')


    return render(request,"register.html")
def index(request):
    return render(request,"index.html")



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return  render(request,'login.html')

def form(request):
    if request.method=='POST':
      name=request.POST.get('name', )
      dob=request.POST.get('dob', )
      age = request.POST.get('age', )
      gender = request.POST.get('gender', )
      phone = request.POST.get('phone', )
      email = request.POST.get('email', )
      address = request.POST.get('address', )
      department = request.POST.get('department', )
      course= request.POST.get('course', )
      purpose = request.POST.get('purpose', )
      materials = request.POST.get('materials', )
      forms=application(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,department=department,course=course,purpose=purpose,materials=materials)
      forms.save();
    return render(request,'form.html')
def apply(request):
    return render(request,'apply.html')



