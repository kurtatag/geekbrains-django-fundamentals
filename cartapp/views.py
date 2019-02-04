from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpRequest

from cartapp.models import Cart
from mainapp.models import Product


def cart(request: HttpRequest):
    context = {}
    return render(request, 'cartapp/cart.html')


def cart_add(request: HttpRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)

    cart = Cart.objects.filter(user=request.user, product=product).first()

    if not cart:
        cart = Cart(user=request.user, product=product)

    cart.quantity += 1
    cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request: HttpRequest, pk: int):
    context = {}
    return render(request, 'cartapp/cart.html')
