from django.contrib import admin
from .models import Menu,MenuCatagory,Cart

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','catagory','price','image']
    list_filter = ['catagory']
    search_fields = ['name']
    
class MenuCatagoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
class CartAdmin(admin.ModelAdmin):
    list_display = ['menu', 'quantity']
    search_fields = ['menu__name']
    
admin.site.register(Menu,MenuAdmin)
admin.site.register(MenuCatagory,MenuCatagoryAdmin)
admin.site.register(Cart, CartAdmin)
