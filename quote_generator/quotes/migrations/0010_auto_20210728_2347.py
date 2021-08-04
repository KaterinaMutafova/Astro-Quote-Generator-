# Generated by Django 3.2.4 on 2021-07-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0009_author_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfilter',
            name='element',
            field=models.CharField(blank=True, choices=[('', '----'), ('огън', 'огън'), ('земя', 'земя'), ('въздух', 'въздух'), ('вода', 'вода')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='element',
            field=models.CharField(choices=[('', '----'), ('огън', 'огън'), ('земя', 'земя'), ('въздух', 'въздух'), ('вода', 'вода')], max_length=15),
        ),
    ]