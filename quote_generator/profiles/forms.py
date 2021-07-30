from django import forms
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserProfile


# PROFILE THEMES:

bright_theme = 'шарено'
sky_blue_theme = 'синьо небе'
green_theme = 'зелено'
lilac_theme = 'лилаво'
sunny_theme = 'слънчево'

THEME_CHOICES = (
    ('', '------'),
    ('0', 'шарено'),
    ('1', 'синьо небе'),
    ('2', 'зелено'),
    ('3', 'лилаво'),
    ('4', 'слънчево'),
)


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
    theme_profile = forms.ChoiceField(
        label='Избери тема на профила',
        widget=forms.Select,
        choices=THEME_CHOICES,
        required=False,
    )
    class Meta:
        model = UserProfile
        exclude = ('user',)





class LoginForm(forms.Form):
    user = None
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(),
        label=('Потребител')
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(),
        label=('Парола')
    )

    def clean_password(self):
        # username = self.cleaned_data['username']
        # password = self.cleaned_data['password']

        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            self.user.clean()
            raise ValidationError("Грешен потребител или парола.")


    def save(self):
        return self.user





