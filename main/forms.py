from django import forms
from .models import Transaction, Categories
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "type", "amount", "category", "description"]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class UserLoginForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        username = forms.CharField()
        password1 = forms.CharField()
        password2 = forms.CharField()
                
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
        