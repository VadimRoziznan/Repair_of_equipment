from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return HttpResponse("Главная страница")

def equipment_view(request):
    return HttpResponse('Здесть будет список оборудования')
