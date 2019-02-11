from django.urls import path

from adminapp.views import users, categories, products

app_name = 'adminapp'

urlpatterns = [
    path('', categories.index, name='index'),

    # users
    path('users/', users.index, name='users'),
    path('users/create/', users.create, name='user_create'),
    path('users/read/<int:pk>/', users.read, name='user_read'),
    path('users/update/<int:pk>/', users.update, name='user_update'),
    path('users/delete/<int:pk>/', users.delete, name='user_delete'),

    # products
    path('products/', products.index, name='products'),
    path('products/create/', products.create, name='product_create'),
    path('products/read/<int:pk>/', products.read, name='product_read'),
    path('products/list/<str:category>/', products.list_by_category, name='products_by_category'),
    path('products/update/<int:pk>/', products.update, name='product_update'),
    path('products/delete/<int:pk>/', products.delete, name='product_delete'),
    #
    # categories
    path('categories/', categories.index, name='categories'),
    path('categories/create/', categories.create, name='category_create'),
    path('categories/read/<int:pk>/', categories.read, name='category_read'),
    path('categories/update/<int:pk>/', categories.update, name='category_update'),
    path('categories/delete/<int:pk>/', categories.delete, name='category_delete'),


]