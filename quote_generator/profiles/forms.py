from django import forms

from quote_generator.profiles.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'is_complete',)
        labels = {
            'date_of_birth': ('Дата на  раждане'),
            'profile_image': ('Снимка на потребител'),
            'theme_profile': ('Фон на профила'),
            'first_name': ('Име'),
            'last_name': ('Фамилия'),
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }




