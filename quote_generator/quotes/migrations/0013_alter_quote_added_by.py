# Generated by Django 3.2.4 on 2021-07-31 08:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotes', '0012_delete_myfilter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('unknown'), to=settings.AUTH_USER_MODEL),
        ),
    ]
