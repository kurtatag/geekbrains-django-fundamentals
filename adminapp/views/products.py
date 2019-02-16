from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.urls import reverse

from mainapp.models import Product, ProductCategory
from adminapp.forms import ProductEditForm


@user_passes_test(lambda user: user.is_superuser)
def index(request: HttpRequest):
    title = 'products'
    products = Product.objects.all()
    categories = ['all'] + [c.name for c in ProductCategory.objects.all()]

    context = {
        'title': title,
        'products': products,
        'categories': categories
    }
    return render(request, 'adminapp/products/index.html', context)


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):
    title = 'new product'

    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:products'))

    form = ProductEditForm()

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'adminapp/products/create.html', context)


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, pk: int):
    title = 'product: {}'
    product = get_object_or_404(Product, pk=pk)

    fields_to_show = ['id', 'name', 'short_description',
                      'description', 'image']
    product_data = model_to_dict(product, fields_to_show)

    context = {
        'title': title.format(product.name),
        'product': product,
        'product_data': product_data,
    }

    return render(request, 'adminapp/products/read.html', context)


@user_passes_test(lambda user: user.is_superuser)
def list_by_category(request: HttpRequest, category):

    if category == 'all':
        products = Product.objects.all()
    else:
        category_object = get_object_or_404(ProductCategory, name=category)
        products = category_object.products.all()

    data = {'products': []}
    for product in products:
        product_info = {
            'product_id': product.id,
            'product_name': product.name
        }
        data['products'].append(product_info)

    return JsonResponse(data)


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, pk):
    title = 'edit category: {}'
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    form = ProductEditForm(instance=product)

    context = {
        'title': title.format(product.name),
        'form': form,
    }

    return render(request, 'adminapp/products/update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    # product.delete()
    product.is_active = False
    product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
