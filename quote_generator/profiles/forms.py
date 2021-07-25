from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control', 'type': 'text', 'align': 'center', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'Email'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError("Email is required!")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder':'password'})
    )
