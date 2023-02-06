from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Electronic medical record")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')