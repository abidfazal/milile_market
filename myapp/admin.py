from django.contrib import admin
from .models import Menu,MenuCatagory

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','catagory','price','image']
    list_filter = ['catagory']
    search_fields = ['name']
    
class MenuCatagoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
admin.site.register(Menu,MenuAdmin)
admin.site.register(MenuCatagory,MenuCatagoryAdmin)
