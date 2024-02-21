# yourappname/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        label='Username',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': 'This username is already taken. Please choose a different one.',
        }
    )
    
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        help_text='Required. Enter a valid email address.',
        error_messages={
            'unique': 'A user with this email address already exists.',
        }
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        help_text='Required. Your password can’t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can’t be a commonly used password.',
        error_messages={
            'password_mismatch': 'The two password fields didn’t match.',
        }
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        help_text='Enter the same password as before, for verification.',
        error_messages={
            'password_mismatch': 'The two password fields didn’t match.',
        }
    )
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
    )

    