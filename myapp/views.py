from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Menu,MenuCatagory
from .forms import MenuForm

# Create your views here.
def home(reqiest):
    data = Menu.objects.all()
    context = {
        'data':data
    }
    return render(reqiest,'home.html',context)

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        catagory_id = request.POST.get('catagory')
        catagory = MenuCatagory.objects.get(id=catagory_id)
        price = request.POST.get('price')
        
        description = request.POST.get('description')
        available = request.POST.get('available')
        print(available)
        type = request.POST.get('type')
        image = request.FILES['image']
        
        menu_item = Menu(name=name, price=price, description=description, catagory=catagory, type=type, image=image)
        menu_item.save()
        
        return redirect('home')
    else:
        catagories = MenuCatagory.objects.all()
        form = MenuForm()
        context = {
            'form': form,
        }

        return render(request, 'add_items_page.html', context)
