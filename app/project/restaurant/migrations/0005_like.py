# Generated by Django 2.0.3 on 2018-05-02 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0004_restaurant_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(verbose_name='like')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to='restaurant.RestaurantReview', verbose_name='review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]