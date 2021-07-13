from django.urls import path
from . import views

urlpatterns = [
    path('adminlogin.html', views.adminlogin, name='adminlogin'),
    path('adminindex.html', views.adminindex, name='adminindex'),
    path('adminstudentdetails.html', views.adminstudentdetails, name='adminstudentdetails'),
    path('adminuserdetails.html', views.adminuserdetails, name='adminuserdetails'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('register.html', views.register, name='register'),
    path('adminpaymentlist.html', views.adminpaymentlist, name='adminpaymentlist'),
    path('libraryuserdetails.html', views.libraryuserdetails, name='libraryuserdetails'),
    path('libraryuserregister.html', views.libraryuserregister, name='libraryuserregister'),

]
