# Generated by Django 4.1.7 on 2023-04-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_rename_uname_userinfo_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='username',
            new_name='user_name',
        ),
    ]
