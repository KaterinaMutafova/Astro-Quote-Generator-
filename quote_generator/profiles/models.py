from django.contrib.auth.models import User
from django.db import models

# Create your models here.

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


class UserProfile(models.Model):
    date_of_birth = models.DateTimeField()
    # date_of_registration = models.DateTimeField()
    # first_name = models.CharField(
    #     max_length=20,
    # )
    # last_name = models.CharField(
    #     max_length=20,
    # )
    # age = models.PositiveIntegerField(
    #     null=True,
    #     blank=True,
    # )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    theme_profile = models.CharField(
        max_length=20,
        choices=THEME_CHOICES,
        blank=True,
        null=True,
        default=1,
    )
    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )







# class Profile(models.Model):
#     first_name = models.CharField(
#         max_length=20,
#     )
#     last_name = models.CharField(
#         max_length=20,
#     )
#     age = models.PositiveIntegerField(
#         null=True,
#         blank=True,
#     )
#     image_url = models.URLField(
#         null=True,
#         blank=True,
#     )

