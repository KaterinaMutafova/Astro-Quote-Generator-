from django.contrib.auth.models import User
from django.db import models
from quote_generator.quotes.models.choices import ZODIAC_CHOICES, ELEMENT_CHOICES


# Create your models here.
from django.db.models import Choices


class Quote(models.Model):


    quote = models.TextField(
        null=False,
        blank=False,
    )
    author = models.ForeignKey('quotes.Author', related_name='quotes', on_delete=models.SET('unknown'))

    sign = models.CharField(
        max_length=20,
        choices=ZODIAC_CHOICES,
        null=True,
        blank=True,
    )
    element = models.CharField(
        max_length=15,
        choices=ELEMENT_CHOICES,
    )
    image = models.ImageField(
        upload_to='quotes_pics',
        null=True,
        blank=True,
    )
    added_by = models.ForeignKey(
        User,
        on_delete=models.SET('unknown'),
    )



