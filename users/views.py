from django.shortcuts import render, redirect
from .models import User,Task
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        MobileNumber=request.POST.get('Mobile')
        password=request.POST.get('password')
        User.objects.create_user(name=name,
                                 email=email,
                                 mobile=MobileNumber,
                                 password=password
                                 )
        
        messages.success(request, "User created successfully")
        return redirect('users:login')
    return render(request,'register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=authenticate(email=email,password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Logged in successfully")
        return redirect('users:dashboard')
    return render(request,'login_user.html')

def logout_user(request):
    logout(request)
    return redirect('users:home')

@login_required
def dashboard(request):
    tasks=Task.objects.all()
    return render(request,'dashboard/task_list.html',{'tasks':tasks})

def home_page(request):
    return render(request,'home_page.html')

def assign_task(request):
    if request.method == 'POST':
        name=request.POST.get('task')
        assign_to=request.POST.get('assign_to')
        task = Task.objects.create(name=name, assigned_to_id=assign_to, assigned_by=request.user)
        task.save()
        return redirect("/user/dashboard/")
    users = User.objects.all()
    return render(request, 'dashboard/asign_task.html', {'users': users})


