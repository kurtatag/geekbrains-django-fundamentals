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

    # get managers for products & categories
    categories = ProductCategory.objects
    products = Product.objects

    # prepare a list of categories for "product category menu"
    product_category_list = ['all'] + [c.name for c in categories.all()]

    # prepare a list of products for a case when a specific category is chosen
    if current_product_category == 'all':
        product_list = products.all()
    else:
        product_list = products.filter(category__name=current_product_category)

    # prepare cart info to be displayed on the site navigation menu
    cart_info = {
        'items_total': 0,
        'price_total': 0
    }

    if request.user.is_authenticated:
        cart_info['items_total'] = Cart.cart_items_total(user=request.user)
        cart_info['price_total'] = Cart.cart_price_total(user=request.user)

    # prepare the context for the template
    context = {
        'title': 'products',
        'site_navigation_links': site_navigation_links,
        'product_category_list': product_category_list,
        'current_product_category': current_product_category,
        'product_list': product_list,
        'cart_info': cart_info
    }

    return render(request, 'mainapp/products.html', context)


def product_details(request: HttpRequest, product_id):

    product = get_object_or_404(Product, pk=product_id)

    # prepare a list of related products
    related_products = Product.objects \
                              .filter(category=product.category) \
                              .exclude(pk=product.pk)

    # prepare cart info to be displayed on the site navigation menu
    cart_info = {
        'items_total': 0,
        'price_total': 0
    }

    if request.user.is_authenticated:
        cart_info['items_total'] = Cart.cart_items_total(user=request.user)
        cart_info['price_total'] = Cart.cart_price_total(user=request.user)

    # prepare the context for the template
    context = {
        'title': 'product details',
        'site_navigation_links': site_navigation_links,
        'product': product,
        'related_products': related_products,
        'cart_info': cart_info
    }

    return render(request, 'mainapp/product_details.html', context)


def contact(request: HttpRequest):
    context = {
        'title': 'contact',
        'site_navigation_links': site_navigation_links
    }
    return render(request, 'mainapp/contact.html', context)
