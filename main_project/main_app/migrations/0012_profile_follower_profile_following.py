# Generated by Django 5.0.1 on 2024-03-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_rename_post_like_fk_post_rename_user_like_fk_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]