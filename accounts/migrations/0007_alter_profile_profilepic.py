# Generated by Django 3.2.4 on 2021-07-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='profiles/'),
        ),
    ]