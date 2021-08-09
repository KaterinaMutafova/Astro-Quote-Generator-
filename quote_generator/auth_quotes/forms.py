from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm

from quote_generator.shared.validators import has_email

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label= ("Парола"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                # 'autocomplete': 'new-password',
                   'class': 'form-control',
                   }
        ),

        # help_text=password_validation.password_validators_help_text_html(),

    )
    password2 = forms.CharField(
        label=("Потвърждение на парола"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                # 'autocomplete': 'new-password',
                   'class': 'form-control'
                   }
        ),

        # help_text=("Въведете същата парола за  валидация."),
    )
    error_messages = {
        'password_mismatch': ('Двете пароли не  съвпадат.'),
    }
    class Meta:
        model = UserModel
        fields = ('email',)
        widgets = {
            # 'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'align': 'center', 'placeholder': 'username'}),
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'type':'text',
                    'align':'center', 'placeholder':'Email'}),

        }
        labels = {
            'username': ('Потребител')
        }
        validators = [has_email],
        error_messages = {
            'has_email': ('Няма въведен имейл.'),
        }


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Трябва да въведете email.")
        return email



# AuthenticationForm

class LoginForm(forms.Form):
    user = None
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label=('Въведете вашия email'),
        validators=[has_email],
        error_messages={'has_email': 'Няма въведен email адрес.'},
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(),
        label=('Въведете парола'),

    )
    validators = [],
    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        # 'inactive': ("This account is inactive."),
    }

    def clean_email(self):
        data = self.cleaned_data['email']
        if not data:
            raise forms.ValidationError("Въведете email.")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if not data:
            raise forms.ValidationError("Please enter your password")
        return data

    def clean(self):
        try:
            email = UserModel.objects.get(email__iexact=self.cleaned_data['email']).email
        except UserModel.DoesNotExist:
            raise forms.ValidationError("No such email registered")
        password = self.cleaned_data['password']

        self.user = authenticate(username=email, password=password)
        if self.user is None or not self.user.is_active:
            raise forms.ValidationError("Email or password is incorrect")
        return self.cleaned_data



    # def clean_password(self):
    #     self.user = authenticate(
    #         email=self.cleaned_data['email'],
    #         password=self.cleaned_data['password'],
    #     )
    #     if not self.user:
    #         raise ValidationError("Грешен email или парола.")


    def save(self):
        return self.user


