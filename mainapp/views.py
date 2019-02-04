from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from cartapp.models import Cart
from .models import Product, ProductCategory

from my_utils import get_data_from_json

site_navigation_links = get_data_from_json('site_navigation_links.json')
product_category_menu_links = get_data_from_json('product_category_menu_links.json')
product_list = get_data_from_json('product_list.json')


def index(request: HttpRequest):
    context = {
        'site_navigation_links': site_navigation_links
    }
    return render(request, 'mainapp/index.html', context)


def products(request: HttpRequest, current_product_category='all'):
    categories = ProductCategory.objects
    products = Product.objects

    product_category_list = ['all'] + [c.name for c in categories.all()]

    if current_product_category == 'all':
        product_list = products.all()
    else:
        product_list = products.filter(category__name=current_product_category)

    cart = []
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)

    context = {
        'title': 'products',
        'site_navigation_links': site_navigation_links,
        'product_category_list': product_category_list,
        'current_product_category': current_product_category,
        'product_list': product_list,
        'cart': cart
    }
    return render(request, 'mainapp/products.html', context)


def product_details(request: HttpRequest, product_id):
    product = get_object_or_404(Product, pk=product_id)
    related_products = Product.objects \
                              .filter(category=product.category) \
                              .exclude(pk=product.pk)

    context = {
        'title': 'product details',
        'site_navigation_links': site_navigation_links,
        'product': product,
        'related_products': related_products
    }
    return render(request, 'mainapp/product_details.html', context)


def contact(request: HttpRequest):
    context = {
        'title': 'contact',
        'site_navigation_links': site_navigation_links
    }
    return render(request, 'mainapp/contact.html', context)
