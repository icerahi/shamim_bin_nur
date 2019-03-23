from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from django.shortcuts import render, redirect


# Create your views here.
from apps.models import Stock, Tem_Stock, Sell_History, Category


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,"You have logged in Successfully")
            return redirect('home')
        else:
            messages.success(request,"Please give correct username and password!")
            return redirect('login')
    return render(request,'login.html')

def user_logout(request):
    messages.success(request,'You have logout successfully')
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


@login_required(login_url='login')
def daily_sell(request):
    option=Category.objects.all()
    cntx={'option':option}

    if request.method=='POST':
        name=request.POST.get('customar_name')
        item=request.POST.get('item_name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        add=Tem_Stock(customar_name=name,item_name=item,quantity=quantity,price=price).save()
        return redirect('daily_sell')
    if request.method=='GET':
        tem_data=Tem_Stock.objects.all()
        total=Tem_Stock.objects.all().aggregate(Sum('price'))
        customar_name=tem_data.first()
        context={'tem_data':tem_data,
                 'total':total['price__sum'],
                 'customar_name':customar_name}

    return render(request,'daily_sell.html',context,cntx)


def clear(request):

    tem_data=Tem_Stock.objects.all()
    for i in tem_data:
        data=Sell_History(customar_name=i.customar_name,item_name=i.item_name,quantity=i.quantity,price=i.price).save()
    Tem_Stock.objects.all().delete()
    return redirect('daily_sell')


@login_required(login_url='login')
def stock(request):
    items=Stock.objects.all()
    context={'items':items}
    return render(request,'stock.html',context)


