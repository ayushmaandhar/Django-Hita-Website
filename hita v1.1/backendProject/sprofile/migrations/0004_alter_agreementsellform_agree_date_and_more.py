# Generated by Django 4.0.1 on 2022-02-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprofile', '0003_agreementsellform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreementsellform',
            name='agree_date',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterField(
            model_name='agreementsellform',
            name='bal_date',
            field=models.DateField(max_length=30),
        ),
    ]
