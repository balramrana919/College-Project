from django import forms
from Accounts.models import usersaccount, students
from AdminApp.models import adminModel
from LibraryApp.models import libraryuserModel


class userAccountForm(forms.ModelForm):
    class Meta:
        model = usersaccount
        fields = '__all__'


class libraryuserForm(forms.ModelForm):
    class Meta:
        model = libraryuserModel
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'


class AdminForm(forms.ModelForm):
    class Meta:
        model = adminModel
        fields = '__all__'