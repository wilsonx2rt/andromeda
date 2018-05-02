# Generated by Django 2.0.3 on 2018-05-01 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project.restaurant.helpers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_code',
                 models.CharField(blank=True, default=project.restaurant.helpers.code_generator, max_length=15,
                                  unique=True, verbose_name='registration_code')),
                ('email', models.CharField(max_length=254, unique=True, verbose_name='email_address')),
                ('location', models.CharField(blank=True, max_length=58, verbose_name='location')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='phone_number')),
                ('things_I_love', models.CharField(blank=True, max_length=50, verbose_name='things_I_love')),
                ('description', models.CharField(blank=True, max_length=3000, verbose_name='description')),
                ('joined_date', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='../profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile',
                                              to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]