from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2','address','user_role','gender','phone']
        widgets = {
            'user_role': forms.RadioSelect(),
            'gender': forms.RadioSelect(),
        }
class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}
        ),
    )


class OTPVerificationForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        label="Enter OTP",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your otp"}
        ),
    )
