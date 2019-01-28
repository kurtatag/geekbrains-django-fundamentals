from django.shortcuts import render
from django.http import HttpRequest
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

    context = {
        'title': 'products',
        'site_navigation_links': site_navigation_links,
        'product_category_list': product_category_list,
        'current_product_category': current_product_category,
        'product_list': product_list
    }
    return render(request, 'mainapp/products.html', context)


def contact(request: HttpRequest):
    context = {
        'title': 'contact',
        'site_navigation_links': site_navigation_links
    }
    return render(request, 'mainapp/contact.html', context)
