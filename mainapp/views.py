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


def products(request: HttpRequest, current_product_type='all'):

    product_type_menu_links = [
        {'url_param': 'all', 'name': 'все'},
        {'url_param': 'home', 'name': 'дом'},
        {'url_param': 'office', 'name': 'офис'},
        {'url_param': 'modern', 'name': 'модерн'},
        {'url_param': 'classic', 'name': 'классика'}
    ]

    related_products = [
        {
            'id': 11,
            'description_title': 'Стул повышенного качества',
            'description_text': 'Не оторваться.'
        },
        {
            'id': 21,
            'description_title': 'Стул повышенного качества',
            'description_text': 'Не оторваться.'
        },
        {
            'id': 31,
            'description_title': 'Стул повышенного качества',
            'description_text': 'Не оторваться.'
        },
    ]

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
