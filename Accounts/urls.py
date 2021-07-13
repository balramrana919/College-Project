from django.urls import path
from . import views

urlpatterns = [
    path('details.html', views.details, name='details'),
    path('login.html', views.login, name='login'),
    path('logout.html', views.logout, name='logout'),
    path('studdetails.html', views.studdetails, name='studdetails'),
    path('studentregister.html', views.studentregister, name='studentregister'),
    path('studprofile.html', views.studprofile, name='studprofile'),
    path('payment.html', views.payment, name='payment'),
    path('paymentdetails.html', views.paymentdetails, name='paymentdetails'),
    path('paymentpage.html', views.paymentpage, name='paymentpage'),
    path('admission.html', views.admission, name='admission'),
    path('paymentlist.html', views.paymentlist, name='paymentlist'),
    path('makepayment.html', views.makepayment, name='makepayment'),

]
