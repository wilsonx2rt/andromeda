# Generated by Django 2.0.3 on 2018-05-03 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0007_auto_20180502_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='category'),
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
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'review')},
        ),
        migrations.AddField(
            model_name='likecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user_c', to='restaurant.Comment', verbose_name='comment'),
        ),
        migrations.AddField(
            model_name='likecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user_c', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterUniqueTogether(
            name='likecomment',
            unique_together={('user', 'comment')},
        ),
    ]
