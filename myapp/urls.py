from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_item/',views.add_item,name='add_item'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('item-details/<int:item_id>/', views.item_details, name='item_details'),
    path('order/<int:item_id>', views.order_item, name='order'),
]
