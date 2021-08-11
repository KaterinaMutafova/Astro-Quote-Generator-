from django.contrib.auth import get_user_model
from django.db import models
from quote_generator.quotes.models.choices import ZODIAC_CHOICES, ELEMENT_CHOICES


# Create your models here.

from quote_generator.shared.validators import has_quote

UserModel = get_user_model()

class Quote(models.Model):


    quote = models.TextField(
        null=False,
        blank=False,
        validators=[has_quote],
        error_messages={'has_quote': 'Това поле е задължително'}
    )
    author = models.ForeignKey(
        'quotes.Author',
        related_name='quotes',
        on_delete=models.SET('unknown'),
        blank=False,
    )

    sign = models.CharField(
        max_length=20,
        choices=ZODIAC_CHOICES,
        null=True,
        blank=False,
    )
    element = models.CharField(
        max_length=15,
        choices=ELEMENT_CHOICES,
        null=True,
        blank=False,
    )
    image = models.ImageField(
        upload_to='quotes_pics',
        null=True,
        blank=True,
    )
    added_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET('unknown'),
        null=True,
        blank=True,
    )



