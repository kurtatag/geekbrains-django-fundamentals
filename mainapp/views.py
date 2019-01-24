from django.shortcuts import render
from django.http import HttpRequest

site_menu_links = [
    {'path_name': 'index', 'name': 'домой'},
    {'path_name': 'products', 'name': 'продукты'},
    {'path_name': 'contact', 'name': 'контакты'}
]


def index(request: HttpRequest):
    context = {
        'site_menu_links': site_menu_links
    }
    return render(request, 'mainapp/index.html', context)


def products(request: HttpRequest):
    context = {
        'title': 'Каталог',
        'site_menu_links': site_menu_links
    }
    return render(request, 'mainapp/products.html', context)


def contact(request: HttpRequest):
    context = {
        'title': 'Контакты',
        'site_menu_links': site_menu_links
    }
    return render(request, 'mainapp/contact.html', context)
