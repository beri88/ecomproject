from django.shortcuts import render,redirect
from django.core.cache import cache
from .models import Product,CartItem 

def product_list(request):
   # products=cache.get('products')
    #if products is None:
        
        products = Product.objects.all()
        #cache.set('products',product_list,900)
        return render(request, 'prod_list.html', {'products': products})


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            user=request.user
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart')

def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = []

    return render(request, 'cart.html', {'cart_items': cart_items})



