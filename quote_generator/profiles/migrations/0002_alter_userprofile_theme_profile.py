# Generated by Django 3.2.4 on 2021-08-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='theme_profile',
            field=models.CharField(blank=True, choices=[('', '------'), ('0', 'шарено небенце'), ('1', 'синьо звездно небе'), ('2', 'зелено небе'), ('3', 'лилав залез'), ('4', 'слънчево е!'), ('5', 'оооранжево небето'), ('6', 'сива буря')], default=1, max_length=20, null=True),
        ),
    ]