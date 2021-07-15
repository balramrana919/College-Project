from django.urls import path
from . import views

urlpatterns = [
    path('libraryindex.html', views.libraryindex, name='libraryindex'),
    path('librarylogin.html', views.librarylogin, name='librarylogin'),
    path('librarylogout/', views.librarylogout, name='librarylogout'),
    path('books.html', views.Books, name='books'),
    ]
