from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('news.html', views.news, name='news'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('services.html', views.services, name='services'),
    path('team.html', views.team, name='team'),
    path('testimonials.html', views.testimonials, name='testimonials'),
    path('faculty.html', views.faculty, name='faculty'),
]
