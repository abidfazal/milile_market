from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Menu,MenuCatagory,Cart, Order
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
    

def item_details(request, item_id):
    try:
        item = Menu.objects.get(id=item_id)
        related_items = Menu.objects.filter(catagory=item.catagory).exclude(id=item_id)[:4]  # Get 4 related items
        context = {
            'item': item,
            'related_items': related_items
        }
        return render(request, 'items_details.html', context)
    except Menu.DoesNotExist:
        return HttpResponse("Item not found", status=404)


@require_POST
@csrf_exempt  
def order_item(request, item_id):
    print("Order item view called")
    try:
        data = json.loads(request.body)
        address = data.get('address', 'No address provided')
        quantity = int(data.get('quantity', 1))
        phone = data.get('phone', 'No phone number provided')
        item = Menu.objects.get(id=item_id)
        order_item = Order(menu=item, quantity=quantity, address=address, phone=phone)
        order_item.save()
        return redirect('home')  # Redirect to home or wherever you want after ordering
    except Menu.DoesNotExist:
        return HttpResponse("Item not found", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)