from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from Accounts.models import usersaccount, students, Fees
from Accounts.forms import userAccountForm, FeeForm
from django.contrib import messages
from django.views.decorators.cache import cache_control



# Login for Users
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == 'POST':
        try:
            userdetails = usersaccount.objects.get(username=request.POST['username'], password=request.POST['password'])
            request.session['username'] = userdetails.username
            return render(request, 'studentregister.html')
        except usersaccount.DoesNotExist as e:
            messages.success(request, 'Username / Password invalid..')
    return render(request, 'login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Logout for users
def logout(request):
    auth.logout(request)
    return redirect('/accounts/login.html')


#Users details
def details(request):
    usersaccounts = usersaccount.objects.all()
    return render(request, 'details.html', {'usersaccounts': usersaccounts})


def studprofile(request, id):
    studs = students.objects.get(id=id)
    return render(request, 'studprofile.html', {'studs': studs})


# New Student Registration (student dash) after user login......
def studentregister(request):
    if request.session._session:
        if request.method == 'POST':
            studentID = request.POST['studentID']
            FirstName = request.POST['FirstName']
            LastName = request.POST['LastName']
            DateOfAdmission = request.POST['DateOfAdmission']
            regNo = request.POST['regNo']
            perAddress = request.POST['perAddress']
            tempAddress = request.POST['tempAddress']
            gender = request.POST['gender']
            contact = request.POST['contact']
            ParentCont = request.POST['ParentCont']
            email = request.POST['email']
            FatherName = request.POST['FatherName']
            GrandFatherName = request.POST['GrandFatherName']
            profileImg = request.FILES['profileImg']
            stud = students(studentID=studentID, FirstName=FirstName, LastName=LastName, DateOfAdmission=DateOfAdmission, regNo=regNo,
                            perAddress=perAddress, tempAddress=tempAddress, gender=gender, contact=contact, ParentCont=ParentCont,
                            email=email, FatherName=FatherName, GrandFatherName=GrandFatherName, profileImg=profileImg)
            stud.save()

            messages.success(request, 'New Student registration details saved successfully.....')
            return render(request, 'studentregister.html')
        else:
            return render(request, 'studentregister.html')
    else:
        return redirect('login.html')


#Student details list
def studdetails(request):
    if request.session._session:
        studentss = students.objects.all()
        return render(request, 'studdetails.html', {'studentss': studentss})
    else:
        return redirect('login.html')

# student payment
def payment(request):
    return render(request, 'payment.html')


def paymentdetails(request):
    if request.method == 'POST':
        try:
            fe = Fees.objects.get(studentss_id=request.POST['studentss_id'])
            return render(request, 'paymentdetails.html', {'fe': fe})
        except Fees.DoesNotExist as e:
            messages.success(request, 'StudentAdmission not done...!')
    return render(request, 'payment.html')


def paymentpage(request):
     if request.method == 'POST':
         studentss_id = request.POST.get("studentss")
         studentss = Fees.objects.get(studentss_id=studentss_id)
         form = FeeForm(request.POST, instance=studentss)
         if form.is_valid():
             form.save()
         return render(request, 'paymentlist.html', {'studentsss': students.objects.all(), 'msg': 'Fee Payment Success'})
     else:
         return render(request, 'paymentpage.html', {'studentsss': students.objects.all()})


def admission(request):
    if request.method == 'POST':
        lastpaidmonth = request.POST.get("lastpaidmonth")
        duetobepaid = request.POST.get("duetobepaid")
        studentss_id = request.POST.get("studentss")
        studentss = students.objects.get(id=studentss_id)
        Fees.objects.create(lastpaidmonth=lastpaidmonth, duetobepaid=duetobepaid, studentss=studentss)
        return render(request, 'admission.html', {'studentsss': students.objects.all(), 'msg': 'Admission Successful..........'})
    else:
        return render(request, 'admission.html', {'studentsss': students.objects.all()})


def paymentlist(request):
    fes = Fees.objects.all()
    return render(request, 'paymentlist.html', {'fes': fes})


def makepayment(request, id):
    fes = Fees.objects.get(id=id)
    return render(request, 'makepayment.html', {'fes': fes})


def updatepayment(request):
    if request.method == 'POST':
        studentss_id = request.POST.get("studentss")
        studentss = Fees.objects.get(studentss_id=studentss_id)
        form = FeeForm(request.POST, instance=studentss)
        if form.is_valid():
            form.save()
        return redirect('/accounts/paymentlist.html')
    else:
        return render(request, 'makepayment.html')
