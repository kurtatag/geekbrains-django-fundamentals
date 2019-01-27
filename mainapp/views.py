from django.shortcuts import render
from django.http import HttpRequest

from my_utils import get_data_from_json

site_navigation_links = get_data_from_json('site_navigation_links.json')
product_category_menu_links = get_data_from_json('product_category_menu_links.json')
related_products = get_data_from_json('related_products.json')


def index(request: HttpRequest):
    context = {
        'site_navigation_links': site_navigation_links
    }
    return render(request, 'mainapp/index.html', context)


def products(request: HttpRequest, current_product_category='all'):
    context = {
        'title': 'Каталог',
        'site_navigation_links': site_navigation_links,
        'product_category_menu_links': product_category_menu_links,
        'current_product_category': current_product_category,
        'related_products': related_products
    }
    return render(request, 'mainapp/products.html', context)


def contact(request: HttpRequest):
    context = {
        'title': 'Контакты',
        'site_navigation_links': site_navigation_links
    }
    return render(request, 'mainapp/contact.html', context)
