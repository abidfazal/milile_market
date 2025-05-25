from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add_item/',views.add_item,name='add_item'),
]
