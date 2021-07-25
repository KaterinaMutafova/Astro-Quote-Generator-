from django.db import models
from quote_generator.quotes.models.choices import ZODIAC_CHOICES, ELEMENT_CHOICES


class Author(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    profession = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to='authors_pics',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'