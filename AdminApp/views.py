from django.shortcuts import render, redirect

from Accounts.forms import userAccountForm, StudentForm
from AdminApp.forms import libraryuserForm
from AdminApp.models import adminModel
from LibraryApp.models import libraryuserModel
from Accounts.models import usersaccount, students, Fees
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminlogin(request):
    if request.method == 'POST':
        try:
            userdetails = adminModel.objects.get(username=request.POST['username'], password=request.POST['password'])
            request.session['username'] = userdetails.username
            return render(request, 'adminindex.html')
        except adminModel.DoesNotExist as e:
            messages.success(request, 'Username / Password invalid..')
    return render(request, 'adminlogin.html')



# Logout for admin
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminlogout(request):
    auth.logout(request)
    return redirect('/adminapp/adminlogin.html')


def adminindex(request):
    return render(request, 'adminindex.html')


def adminstudentdetails(request):
    stu = students.objects.all()
    return render(request, 'adminstudentdetails.html', {'stu': stu})


def adminuserdetails(request):
    usr = usersaccount.objects.all()
    return render(request, 'adminuserdetails.html', {'usr': usr})


def adminpaymentlist(request):
    fes = Fees.objects.all()
    return render(request, 'adminpaymentlist.html', {'fes': fes})


# New users Registration......
def register(request):
    if request.method == 'POST':
        if request.POST.get('userID') and request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('username') and request.POST.get('password') and request.POST.get('contact') and request.POST.get('email'):
            saverec = usersaccount()
            saverec.userID = request.POST.get('userID')
            saverec.firstname = request.POST.get('firstname')
            saverec.lastname = request.POST.get('lastname')
            saverec.username = request.POST.get('username')
            saverec.password = request.POST.get('password')
            saverec.contact = request.POST.get('contact')
            saverec.email = request.POST.get('email')
            saverec.save()

            messages.success(request, 'New user registration details saved successfully.....')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


# users edit
def edit(request, id):
    users = usersaccount.objects.get(id=id)
    return render(request, 'edit.html', {'users': users})


# users details update
def update(request, id):
    users = usersaccount.objects.get(id=id)
    form = userAccountForm(request.POST, instance=users)
    if form.is_valid():
        form.save()
        return redirect('/adminapp/adminuserdetails.html')
    return render(request, 'edit.html', {'users': users})


# delete users
def delete(request, id):
    users = usersaccount.objects.get(id=id)
    users.delete()
    return redirect('/adminapp/adminuserdetails.html')


def studdelete(request, id):
    studs = students.objects.get(id=id)
    studs.delete()
    return redirect('/adminapp/adminstudentdetails.html')


def libraryuserdetails(request):
    usr = libraryuserModel.objects.all()
    return render(request, 'libraryuserdetails.html', {'usr': usr})


def libraryuserregister(request):
    if request.method == 'POST':
        if request.POST.get('L_ID') and request.POST.get('fullname') and request.POST.get('username') and request.POST.get('password') and request.POST.get('contact') and request.POST.get('email') and request.POST.get('address'):
            saverec = libraryuserModel()
            saverec.L_ID = request.POST.get('L_ID')
            saverec.fullname = request.POST.get('fullname')
            saverec.username = request.POST.get('username')
            saverec.password = request.POST.get('password')
            saverec.address = request.POST.get('address')
            saverec.contact = request.POST.get('contact')
            saverec.email = request.POST.get('email')
            saverec.save()

            messages.success(request, 'New Library user registered successfully..')
            return render(request, 'libraryuserregister.html')
    else:
        return render(request, 'libraryuserregister.html')


def libraryuserdelete(request, id):
    studs = libraryuserModel.objects.get(id=id)
    studs.delete()
    return redirect('/adminapp/libraryuserdetails.html')

# library users edit
def libraryuseredit(request, id):
    users = libraryuserModel.objects.get(id=id)
    return render(request, 'libraryuseredit.html', {'users': users})


# library users details update
def libraryuserupdate(request, id):
    users = libraryuserModel.objects.get(id=id)
    form = libraryuserForm(request.POST, instance=users)
    if form.is_valid():
        form.save()
        return redirect('/adminapp/libraryuserdetails.html')
    return render(request, 'libraryuseredit.html', {'users': users})
