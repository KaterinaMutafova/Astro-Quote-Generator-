import os

from django import forms
from django.conf import settings

from quote_generator.profiles.models import UserProfile


class ProfileForm(forms.ModelForm):
    def save(self, commit=True):
        old_profile = UserProfile.objects.get(pk=self.instance.pk)
        new_image = self.files.get('image')
        old_image = str(old_profile.image)
        old_image_path = os.path.join(settings.MEDIA_ROOT, old_image)
        if commit and new_image and old_image:
            if old_image:
                os.remove(old_image_path)
        return super().save(commit=commit)

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
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }




