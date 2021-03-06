# Generated by Django 3.2.4 on 2021-08-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='element',
            field=models.CharField(choices=[('', '------'), ('огън', 'огън'), ('земя', 'земя'), ('въздух', 'въздух'), ('вода', 'вода')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='sign',
            field=models.CharField(choices=[('', '------'), ('овен', 'овен'), ('телец', 'телец'), ('близнаци', 'близнаци'), ('рак', 'рак'), ('лъв', 'лъв'), ('дева', 'дева'), ('везни', 'везни'), ('скорпион', 'скорпион'), ('стрелец', 'стрелец'), ('козирог', 'козирог'), ('водолей', 'водолей'), ('риби', 'риби')], max_length=20, null=True),
        ),
    ]
