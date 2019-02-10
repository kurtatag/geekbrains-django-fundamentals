from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def create(request: HttpRequest):
    return HttpResponse('action -> create')


def read(request: HttpRequest, pk):
    return HttpResponse('action -> read')


def list_by_category(request: HttpRequest, category):
    return HttpResponse('action -> list_by_category')


def update(request: HttpRequest, pk):
    return HttpResponse('action -> update')


def delete(request: HttpRequest, pk):
    return HttpResponse('action -> delete')
