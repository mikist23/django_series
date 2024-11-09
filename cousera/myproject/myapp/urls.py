from django.urls import path
from . import views

urlpatterns = [
    # path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
    path('about/', views.About, name ='about'),
    path('home/', views.Home, name ='home'),
    path('menu/', views.Menu, name ='menu'),
    path('book/', views.Book, name='book'),
    path('booking/', views.form_view),

]