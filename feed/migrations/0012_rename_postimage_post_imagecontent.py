# Generated by Django 3.2.4 on 2021-07-16 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0011_post_postimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postimage',
            new_name='imagecontent',
        ),
    ]
