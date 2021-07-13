from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def news(request):
    return render(request, 'news.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def services(request):
    return render(request, 'services.html')


def team(request):
    return render(request, 'team.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def faculty(request):
    return render(request, 'faculty.html')



