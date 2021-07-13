"""COLLEGEPROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Accounts import views as account_views
from AdminApp import views as admin_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('adminapp/', include('AdminApp.urls')),
    path('libraryapp/', include('LibraryApp.urls')),
    path('home/', include('Home.urls')),
    path('register/', admin_views.register),
    path('delete/', admin_views.delete),
    path('adminuserdetails/', admin_views.adminuserdetails),
    path('studdetails', account_views.studdetails),
    path('details/', account_views.details),
    path('adminapp/edit/<int:id>', admin_views.edit, name='edit'),
    path('update/<int:id>', admin_views.update),
    path('adminapp/libraryuseredit/<int:id>', admin_views.libraryuseredit, name='libraryuseredit'),
    path('libraryuserupdate/<int:id>', admin_views.libraryuserupdate),
    path('paymentdetails/<int:id>', account_views.paymentdetails),
    path('accounts/makepayment/<int:id>', account_views.makepayment),
    path('updatepayment/', account_views.updatepayment),
    path('studprofile/<int:id>', account_views.studprofile),
    path('delete/<int:id>', admin_views.delete),
    path('studdelete/<int:id>', admin_views.studdelete),
    path('libraryuserdelete/<int:id>', admin_views.libraryuserdelete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

