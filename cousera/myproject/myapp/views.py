from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm
from myapp.models import Menu

# Create your views here.

def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)

# def home(request):
#     return HttpResponse('Welcome to Little Lemon!')

# def about(request):
#     return HttpResponse("About us")

# def menu(request):
#     return HttpResponse('<h1>Menu</h1>')

# def book(request):
#     return HttpResponse('<h1>Make a booking!</h1>')


def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "booking.html", context)


# def about(request):
#     about_content  = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 

#     return render(request, 'about.html', {'content': about_content})

# def menu(request):
#     about_menu = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
#     return render(request, 'menu.html', {"context": about_menu})


# def menu(request):
#      menu_items  = Menu.objects.all()
#      items_dict  = {'menu':menu_items}
#      return render(request, 'menu.html',  items_dict)

    
def Home(request):
    return render(request, 'home.html' )

def Menu(request):
    return render(request, 'menu.html')

def About(request):
    return render(request, 'about.html')

def Book(request):
    return render(request, 'book.html')