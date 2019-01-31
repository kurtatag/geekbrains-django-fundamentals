from django.urls import path

import authapp.views as authapp_views

app_name = 'mainapp'

urlpatterns = [
    path('login/', authapp_views.login, name='login'),
    path('logout/', authapp_views.logout, name='logout'),
    path('edit/', authapp_views.edit, name='edit'),
]
