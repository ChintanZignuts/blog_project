from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-green-500 transition',
        'placeholder': 'Enter your email'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-green-500 transition',
        'placeholder': 'Enter your password'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-green-500 transition',
        'placeholder': 'Confirm your password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-green-500 transition',
                'placeholder': 'Enter your username'
            }),
        }