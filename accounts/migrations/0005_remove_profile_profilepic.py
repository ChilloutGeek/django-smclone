# Generated by Django 3.2.4 on 2021-07-16 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profilepic',
        ),
    ]
