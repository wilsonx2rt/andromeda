# Generated by Django 2.0.3 on 2018-05-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='../profile_pictures/', verbose_name='profile_picture'),
        ),
    ]