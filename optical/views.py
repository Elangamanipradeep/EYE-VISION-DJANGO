from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth import authenticate,login ,logout
from optical.form import CustomUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:  # Check if name is not empty
            contact = Contact()
            contact.name = name
            contact.email = request.POST.get('email')
            contact.mobile = request.POST.get('mobile')
            contact.product = request.POST.get('product')
            contact.message = request.POST.get('message')
            contact.save()
    return render(request, "index.html")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('opticals:login') 

def login_user(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('opticals:index')
        else:
            return redirect('opticals:login')
    
    return render(request, 'login.html', {})


def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Sucess You can Login Now ..!")
            return redirect('opticals:login')
    return render(request, 'register.html', {'form':form})


@login_required
def careera(request):
    if request.method == "POST":

        quantity = int(request.POST.get('quantity', 1))
        product_price = 2599
        total_price = quantity * product_price

        orders = Orders(
            ProductName="CAREERA 782",
            Quantity= str(quantity),
            Price=str(total_price),
            Firstname=request.POST.get('Firstname'),
            Lastname=request.POST.get('Lastname'),
            Email=request.POST.get('Email'),
            Phone=request.POST.get('Phone'),
            Address=request.POST.get('Address'),
            City=request.POST.get('City'),
            State=request.POST.get('State'),
            Country=request.POST.get('Country'),
            Pincode=request.POST.get('Pincode'),
        )
        orders.save()
        # messages.success(request,"Order placed Successfully.")

        return render(request, 'Orders/Ordersuccess.html', {})
    return render(request, 'Orders/careera.html', {})

@login_required
def TommyHillfiger(request):
    if request.method == "POST":

        quantity = int(request.POST.get('quantity', 1))
        product_price = 2999
        total_price = quantity * product_price


        orders = Orders(
            ProductName="TOMMY HILFIGER",
            Quantity= str(quantity),
            Price=str(total_price),
            Firstname=request.POST.get('Firstname'),
            Lastname=request.POST.get('Lastname'),
            Email=request.POST.get('Email'),
            Phone=request.POST.get('Phone'),
            Address=request.POST.get('Address'),
            City=request.POST.get('City'),
            State=request.POST.get('State'),
            Country=request.POST.get('Country'),
            Pincode=request.POST.get('Pincode'),
        )
        orders.save()
        # messages.success(request,"Order placed Successfully.")

        return render(request, 'Orders/Ordersuccess.html', {})
    return render(request, 'Orders/Tommyhillfiger.html',{})

@login_required
def Empario(request):
    if request.method == "POST":

        quantity = int(request.POST.get('quantity', 1))
        product_price = 3599
        total_price = quantity * product_price
        
        orders = Orders(
            ProductName="EMPORIO ARMANI",
            Quantity= str(quantity),
            Price=str(total_price),
            Firstname=request.POST.get('Firstname'),
            Lastname=request.POST.get('Lastname'),
            Email=request.POST.get('Email'),
            Phone=request.POST.get('Phone'),
            Address=request.POST.get('Address'),
            City=request.POST.get('City'),
            State=request.POST.get('State'),
            Country=request.POST.get('Country'),
            Pincode=request.POST.get('Pincode'),
       )
        orders.save()
        # messages.success(request,"Order placed Successfully.")

        return render(request, 'Orders/Ordersuccess.html', {})
    return render(request, 'Orders/Emporio.html',{})

@login_required
def Rayban(request):
    if request.method == "POST":

        quantity = int(request.POST.get('quantity', 1))
        product_price = 3599
        total_price = quantity * product_price

        orders = Orders(
            ProductName="RAY-BAN 782",
            Quantity= str(quantity),
            Price=str(total_price),
            Firstname=request.POST.get('Firstname'),
            Lastname=request.POST.get('Lastname'),
            Email=request.POST.get('Email'),
            Phone=request.POST.get('Phone'),
            Address=request.POST.get('Address'),
            City=request.POST.get('City'),
            State=request.POST.get('State'),
            Country=request.POST.get('Country'),
            Pincode=request.POST.get('Pincode'),
        )
        orders.save()
        # messages.success(request,"Order placed Successfully.")

        return render(request, 'Orders/Ordersuccess.html', {})
    return render(request, 'Orders/rayban.html',{})

@login_required
def Fastrack(request):
    if request.method == "POST":

        quantity = int(request.POST.get('quantity', 1))
        product_price = 2799
        total_price = quantity * product_price

        orders = Orders(
            ProductName="FASTRACK",
            Quantity= str(quantity),
            Price=str(total_price),
            Firstname=request.POST.get('Firstname'),
            Lastname=request.POST.get('Lastname'),
            Email=request.POST.get('Email'),
            Phone=request.POST.get('Phone'),
            Address=request.POST.get('Address'),
            City=request.POST.get('City'),
            State=request.POST.get('State'),
            Country=request.POST.get('Country'),
            Pincode=request.POST.get('Pincode'),
        )
        orders.save()
        # messages.success(request,"Order placed Successfully.")

        return render(request, 'Orders/Ordersuccess.html', {})
    return render(request, 'Orders/Fastrack.html',{})

    

