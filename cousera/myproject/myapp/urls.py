from django.urls import path
from . import views

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
    path('about/', views.about, name ='about'),
    path('home/', views.home, name ='home'),
    path('menu/', views.menu, name ='menu'),
    path('book/', views.book),
]