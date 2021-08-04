from django import forms
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label= ("Парола"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Потвърждение на парола"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        # help_text=("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'align': 'center', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'Email'}),
        }
        labels = {
            'username': ('Потребител')
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError("Email is required!")
        return email




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
        label=('Парола'),

    )

    def clean_password(self):
        # username = self.cleaned_data['username']
        # password = self.cleaned_data['password']

        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError("Грешен потребител или парола.")



    def save(self):
        return self.user


