# Generated by Django 4.1 on 2022-09-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='posts',
            field=models.IntegerField(default=0),
        ),
    ]