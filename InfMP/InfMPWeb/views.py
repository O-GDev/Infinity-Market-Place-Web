from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def sellerlogin(request):
    # if request.method == 'POST':

    return render(request, 'sellerlogin.html', {})

def buyerlogin(request):
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