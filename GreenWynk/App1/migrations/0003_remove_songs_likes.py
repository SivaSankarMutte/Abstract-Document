# Generated by Django 3.0 on 2021-07-18 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_songs_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='likes',
        ),
    ]
