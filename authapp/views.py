from django.http import HttpRequest
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from django.contrib import  auth
from django.urls import reverse

from my_utils import get_data_from_json

site_navigation_links = get_data_from_json('site_navigation_links.json')


def login(request: HttpRequest):
    title = 'login'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'site_navigation_links': site_navigation_links,
        'login_form': login_form
    }
    return render(request, 'authapp/login.html', context)


def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def edit(request: HttpRequest):
    title = 'edit user'

    context = {
        'title': title,
        'site_navigation_links': site_navigation_links,
    }
    return render(request, 'authapp/edit.html', context)
