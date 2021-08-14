import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# PROFILE THEMES:

# bright_theme = 'шарено'
# sky_blue_theme = 'синьо небе'
# green_theme = 'зелено'
# lilac_theme = 'лилаво'
# sunny_theme = 'слънчево'
from quote_generator.auth_quotes.models import QuoteUser

THEME_CHOICES = (
    ('', '------'),
    ('0', 'шарено небенце'),
    ('1', 'синьо звездно небе'),
    ('2', 'зелено небе'),
    ('3', 'лилав залез'),
    ('4', 'слънчево е!'),
    ('5', 'оооранжево небето'),
    ('6', 'сива буря'),
)

UserModel = get_user_model()

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
        UserModel,
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
    image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )
    is_complete = models.BooleanField(
        default=False,
    )


from quote_generator.shared.signals import *