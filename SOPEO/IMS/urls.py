from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = "index"),
    path('home/',views.home, name = "Home"),
    path('itemList/',views.itemList, name = "ItemList"),
    path('sellItem/',views.sellItem, name = "SellItem"),
    path('createNewItem/',views.createNewItem, name = "CreateNewItem"),
    path('itemDetails/',views.itemDetails, name = "ItemDetails"),
    path('ordersPlaced/',views.ordersPlaced, name = "OrdersPlaced"),
    path('ordersCancelled/',views.ordersCancelled, name = "ordersCancelled"),
    path('ordersReceived/',views.ordersReceived, name = "ordersReceived"),
    path('itemsSold/',views.itemsSold, name = "itemsSold"),
    path('editItem/',views.editItem, name = "editItem"),
]

