from django import forms
from Accounts.models import usersaccount, students, Fees


class userAccountForm(forms.ModelForm):
    class Meta:
        model = usersaccount
        fields = '__all__'



class StudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'


class FeeForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = '__all__'

