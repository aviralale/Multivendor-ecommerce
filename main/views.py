from django.shortcuts import render, redirect
from django.http import HttpResponse
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items,
    }
    return render(request,'main/index.html', context)
def contact(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request,'main/contact.html',context)

def signup(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    else:
        form = SignupForm()

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'auth/signup.html',context)

def handleLogout(request):
    logout(request)
    return redirect('/')
