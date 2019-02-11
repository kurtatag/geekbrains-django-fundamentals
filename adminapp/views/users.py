from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.urls import reverse

from authapp.models import ShopUser
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm


@user_passes_test(lambda user: user.is_superuser)
def index(request: HttpRequest):
    title = 'users'
    users = ShopUser.objects.all()

    context = {
        'title': title,
        'users': users
    }
    return render(request, 'adminapp/users/index.html', context)


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):
    title = 'new user'

    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))

    form = ShopUserRegisterForm()

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'adminapp/users/create.html', context)


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, pk):
    title = 'user: {}'
    user = get_object_or_404(ShopUser, pk=pk)

    fields_to_show = ['id', 'username', 'email', 'age', 'avatar',
                      'is_superuser', 'is_staff', 'is_active']
    user_data = model_to_dict(user, fields_to_show)

    context = {
        'title': title.format(user.username),
        'user': user,
        'user_data': user_data,
    }

    return render(request, 'adminapp/users/read.html', context)


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, pk):
    title = 'edit user: {}'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        form = ShopUserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))

    form = ShopUserEditForm(instance=user)

    context = {
        'title': title.format(user.username),
        'form': form,
    }

    return render(request, 'adminapp/users/update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    user.delete()
    return HttpResponseRedirect(reverse('admin:users'))
