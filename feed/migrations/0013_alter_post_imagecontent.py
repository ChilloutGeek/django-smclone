# Generated by Django 3.2.4 on 2021-07-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_rename_postimage_post_imagecontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagecontent',
            field=models.ImageField(blank=True, null=True, upload_to='content/'),
        ),
    ]
