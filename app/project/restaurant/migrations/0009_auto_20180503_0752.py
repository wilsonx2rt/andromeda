# Generated by Django 2.0.3 on 2018-05-03 07:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20180502_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterField(
            model_name='restaurantreview',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL, verbose_name='like'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set(),
        ),
    ]
