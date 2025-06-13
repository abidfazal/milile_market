from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_item/',views.add_item,name='add_item'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart')
]
