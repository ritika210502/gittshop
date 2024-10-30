from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from giftshopapp.models import user,product

# Create your views here.
def main(request):
    return render(request,'main.html')

def menu(request):
    return render(request,'menu.html')

def personalized(request):
    pro=product.objects.filter(category__icontains='personalized')
    return render(request,'personalized.html',{'pro':pro})

def cakes(request):
    pro=product.objects.filter(category__icontains='cakes')
    return render(request,'cakes.html',{'pro':pro})

def co_gifts(request):
    pro=product.objects.filter(category__icontains='corporate')
    return render(request,'co_gifts.html',{'pro':pro})

def flower(request):
    pro=product.objects.filter(category__icontains='Flower')
    return render(request,'flower.html',{'pro':pro})

def gourmet(request):
    pro=product.objects.filter(category__icontains='gourmet')
    return render(request,'gourmet.html',{'pro':pro})

def new_arrivals(request):
    pro=product.objects.filter(category__icontains='arrival')
    return render(request,'new_arrivals.html',{'pro':pro})

def plant(request):
    pro=product.objects.filter(category__icontains='plant')
    return render(request,'plant.html',{'pro':pro})

def wishlist(request):
    return render(request,'wishlist.html')
def cart(request):
    return render(request,'cart.html')

def signUp(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        request.session['email']=email
        password=request.POST['password']
        person=user(name=name,email=email,password=password)
        person.save()
        return redirect('main')
    return render(request,'signUp.html')

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        request.session['email']=email
        password=request.POST['password']
        nuser=user.objects.filter(email=email,password=password)
        if not nuser:
            messages.error(request,'username or password are invalid (:\n Please try again')
            return redirect('login')
        return redirect('main')
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')