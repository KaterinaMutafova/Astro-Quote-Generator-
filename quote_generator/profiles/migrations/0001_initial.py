# Generated by Django 3.2.4 on 2021-08-06 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth_quotes.quoteuser')),
                ('theme_profile', models.CharField(blank=True, choices=[('', '------'), ('0', 'шарено'), ('1', 'синьо небе'), ('2', 'зелено'), ('3', 'лилаво'), ('4', 'слънчево'), ('5', 'оранжево небето'), ('6', 'сива буря')], default=1, max_length=20, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
