from django.contrib.auth.models import User
from django.db import models

# Create your models here.


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
    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
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

