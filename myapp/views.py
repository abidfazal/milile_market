from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Menu,MenuCatagory,Cart
from .forms import MenuForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

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


@require_POST
@csrf_exempt  # Optional if you're already handling CSRF via fetch (which you are)
def add_to_cart(request, item_id):
    try:
        data = json.loads(request.body)
        quantity = int(data.get('quantity', 1))
        menu_item = Menu.objects.get(id=item_id)

        cart_item, created = Cart.objects.get_or_create(menu=menu_item, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return JsonResponse({'status': 'success', 'message': 'Item added to cart'})

    except Menu.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Item not found'}, status=404)

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)