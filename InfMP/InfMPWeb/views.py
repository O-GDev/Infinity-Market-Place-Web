from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def sellerlogin(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        #  Authenticate
        user = authenticate(request, username=username, password = password )
        if user is not None:
            login(request, user)
            messages.success(request,"You have successfully logged in!")
            return redirect('')
        else:
            messages.success(request, "There was an error logging in!")
            return redirect('sellerlogin')
    else:
        return render(request, 'sellerlogin.html', {})    

def buyerlogin(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        #  Authenticate
        user = authenticate(request, username=username, password = password )
        if user is not None:
            login(request, user)
            messages.success(request,"You have successfully logged in!")
            return redirect('')
        else:
            messages.success(request, "There was an error logging in!")
            return redirect('buyerlogin')
    else:
        return render(request, 'buyerlogin.html', {}) 



def register_seller(request):   
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authentication
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, "you have successfully logged In!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'sellersignup.html', {'form':form})   
    return render(request, 'sellersignup.html', {'form':form})            

def register_buyer(request):   
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authentication
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, "you have successfully logged In!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'sellersignup.html', {'form':form})   
    return render(request, 'sellersignup.html', {'form':form}) 



def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def help(request):
    return render(request, 'help.html', {})    



def sellerdashboard(request):
    return render(request,'sellerdashboard.html',{})

def buyerdashboard(request):
    return render(request,'buyerdashboard.html',{})