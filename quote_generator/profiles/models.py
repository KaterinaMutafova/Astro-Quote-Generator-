import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# PROFILE THEMES:

# bright_theme = 'шарено'
# sky_blue_theme = 'синьо небе'
# green_theme = 'зелено'
# lilac_theme = 'лилаво'
# sunny_theme = 'слънчево'

THEME_CHOICES = (
    ('', '------'),
    ('0', 'шарено'),
    ('1', 'синьо небе'),
    ('2', 'зелено'),
    ('3', 'лилаво'),
    ('4', 'слънчево'),
    ('5', 'оранжево небето'),
    ('6', 'сива буря'),
)


class UserProfile(models.Model):
    date_of_birth = models.DateTimeField(
        null=True,
        blank=True,
    )
    # date_of_registration = models.DateTimeField()
    first_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
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
    is_complete = models.BooleanField(
        default=False,
    )

