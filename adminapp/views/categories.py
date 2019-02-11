from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.models import ProductCategory
from adminapp.forms import ProductCategoryEditForm


@user_passes_test(lambda user: user.is_superuser)
def index(request: HttpRequest):
    title = 'categories'
    categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'categories': categories
    }

    return render(request, 'adminapp/categories/index.html', context)


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):
    title = 'new category'

    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))

    form = ProductCategoryEditForm()

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'adminapp/categories/create.html', context)


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, pk):
    title = 'category: {}'
    category = get_object_or_404(ProductCategory, pk=pk)
    products = category.products.all()[:5]

    context = {
        'title': title.format(category.name),
        'category': category,
        'products': products,
    }

    return render(request, 'adminapp/categories/read.html', context)


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, pk):
    title = 'edit category: {}'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))

    form = ProductCategoryEditForm(instance=category)

    context = {
        'title': title.format(category.name),
        'form': form,
    }

    return render(request, 'adminapp/categories/update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    category.delete()
    return HttpResponseRedirect(reverse('admin:categories'))
