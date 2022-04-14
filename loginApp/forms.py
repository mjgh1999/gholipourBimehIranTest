from django import forms
from .models import Data, User


class InsertDataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('idNumber', 'branchCode', 'transactionValue')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


