from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from quote_generator.quotes.models import Quote

UserModel = get_user_model()


class Like(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )



