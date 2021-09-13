from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


# class Sign(models.Model):
#     the_user = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE,
#     )
#     sign =

# class Aries(models.Model):
#     the_user = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#     )
#     sign = 'овен'
#     planet_ruler = 'Марс'
#     element = 'огън'
#
#     @property
#     def count_aries(self):
#         return Aries.objects.all().count()


