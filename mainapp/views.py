from django.shortcuts import render
from django.http import HttpRequest

from my_utils import get_data_from_json

site_menu_links = get_data_from_json('site_menu_links.json')
product_type_menu_links = get_data_from_json('product_type_menu_links.json')
related_products = get_data_from_json('related_products.json')


def index(request: HttpRequest):
    context = {
        'site_menu_links': site_menu_links
    }
    return render(request, 'mainapp/index.html', context)


def products(request: HttpRequest, current_product_type='all'):
    context = {
        'title': 'Каталог',
        'site_menu_links': site_menu_links,
        'product_type_menu_links': product_type_menu_links,
        'current_product_type': current_product_type,
        'related_products': related_products
    }
    return render(request, 'mainapp/products.html', context)


def contact(request: HttpRequest):
    context = {
        'title': 'Контакты',
        'site_menu_links': site_menu_links
    }
    return render(request, 'mainapp/contact.html', context)
