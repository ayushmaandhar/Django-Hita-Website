# Generated by Django 4.0.1 on 2022-01-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileForm',
        ),
    ]
