from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from LibraryApp.models import libraryuserModel
from django.contrib import messages, auth


def libraryindex(request):
    return render(request, 'libraryindex.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def librarylogin(request):
    if request.method == 'POST':
        try:
            userdetails = libraryuserModel.objects.get(username=request.POST['username'], password=request.POST['password'])
            request.session['username'] = userdetails.username
            return render(request, 'libraryindex.html')
        except libraryuserModel.DoesNotExist as e:
            messages.success(request, 'Username / Password invalid..')
    return render(request, 'librarylogin.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def librarylogout(request):
    auth.logout(request)
    return redirect('/libraryapp/librarylogin.html')

