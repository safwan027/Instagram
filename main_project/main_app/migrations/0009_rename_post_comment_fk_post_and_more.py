# Generated by Django 5.0.2 on 2024-02-20 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_post_fk_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='fk_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='User',
            new_name='fk_user',
        ),
    ]