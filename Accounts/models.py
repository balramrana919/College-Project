from django.db import models


class usersaccount(models.Model):
    userID = models.CharField(max_length=10)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'useraccounts_db'

class students(models.Model):
    studentID = models.CharField(max_length=10)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    DateOfAdmission = models.DateField()
    regNo = models.CharField(max_length=20)
    perAddress = models.CharField(max_length=30)
    tempAddress = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    contact = models.IntegerField()
    ParentCont = models.IntegerField()
    email = models.EmailField()
    FatherName = models.CharField(max_length=20)
    GrandFatherName = models.CharField(max_length=20)
    profileImg = models.ImageField(max_length=255, upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.regNo

    class Meta:
        db_table = 'students_db'


class Fees(models.Model):
    lastpaidmonth = models.CharField(max_length=10)
    duetobepaid = models.IntegerField(default=True)
    amountpaid = models.IntegerField(default=True)
    advance = models.IntegerField(default=True)
    studentss = models.ForeignKey(students, default=True, on_delete=models.CASCADE)
    class Meta:
        db_table = 'fees_db'


class feesPrice(models.Model):
    Admissionfee = models.IntegerField()
    monthlyfee = models.IntegerField()
    examfee = models.IntegerField()
    class Meta:
        db_table = 'feesprice_db'


