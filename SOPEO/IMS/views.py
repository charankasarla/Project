from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory
# Create your views here.

def index(request):
    
    inventory = Inventory.objects.all()
    return render(request,'index/index.html',{'inventory':inventory})

def home(request):
    return render(request,'home/index.html')

def itemList(request):
    return HttpResponse("This is ItemList Screen")

def sellItem(request):
    return HttpResponse("This is Sellitem Screen")

def createNewItem(request):
    if request == "on":
        name = request.POST['name']
        quantity = request.POST['quantity']
        quantity_sold = request.POST['quantity_sold']
        selling_price = request.POST['selling_price']
        profit_earned = request.POST['profit_earned']
        
        new_item = Inventory(product_name = name,quantity = quantity, quantity_sold = quantity_sold,selling_price = selling_price, profit_earned = profit_earned)
        new_item.save()
    return render(request,'createNewItem/index.html',{})
    #return HttpResponse("This is createNewItem Screen")

def itemDetails(request):
    return HttpResponse("This is itemDetails Screen")

def ordersPlaced(request):
    return HttpResponse("This is ordersPlaced Screen")

def ordersReceived(request):
    return HttpResponse("This is ordersReceived Screen")

def ordersCancelled(request):
    return HttpResponse("This is ordersCancelled Screen")

def itemsSold(request):
    return HttpResponse("This is itemSold Screen")

def editItem(request):
    return HttpResponse("This is editItem Screen")