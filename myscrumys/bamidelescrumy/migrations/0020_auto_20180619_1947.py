# Generated by Django 2.0 on 2018-06-19 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bamidelescrumy', '0019_auto_20180619_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrumygoals',
            old_name='status_id',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='scrumygoals',
            old_name='user_id',
            new_name='user',
        ),
    ]
