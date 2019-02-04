from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpRequest

from cartapp.models import Cart
from mainapp.models import Product
from my_utils import get_data_from_json

site_navigation_links = get_data_from_json('site_navigation_links.json')


def cart(request: HttpRequest):
    cart = Cart.objects.filter(user=request.user)
    context = {
        'title': 'cart',
        'site_navigation_links': site_navigation_links,
        'cart': cart
    }
    return render(request, 'cartapp/cart.html', context)


def cart_add(request: HttpRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)

    cart = Cart.objects.filter(user=request.user, product=product).first()

    if not cart:
        cart = Cart(user=request.user, product=product)

    cart.quantity += 1
    cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request: HttpRequest, pk: int):
    cart_product = get_object_or_404(Cart, pk=pk)

    cart_product.quantity -= 1

    if cart_product.quantity < 1:
        cart_product.delete()
    else:
        cart_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
