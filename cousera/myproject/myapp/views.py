from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)

def home(request):
    return HttpResponse('Welcome to Little Lemon!')

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse('<h1>Menu</h1>')

def book(request):
    return HttpResponse('<h1>Make a booking!</h1>')
