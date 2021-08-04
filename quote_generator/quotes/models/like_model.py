from django.contrib.auth.models import User
from django.db import models
from quote_generator.quotes.models import Quote


class Like(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )