from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    return render(request, 'mainapp/index.html')


def products(request: HttpRequest):
    return render(request, 'mainapp/products.html')


def contact(request: HttpRequest):
    return render(request, 'mainapp/contact.html')
